import array
import logging

from doc_uploader.doc_handlers.interfaces import Document
from doc_uploader.models.datamodels import GraphModel
from doc_uploader.utils import invalid_key_fix, no_quotes_object

from ...factory import DocToDBAdapters
from ...protocols import DocumentToDB

logger = logging.getLogger("app")


# neo4j needs " to be \\" within the contents
def _escape_double_quote(s: str):
    return s.replace('"', '\\"')


class _Neo4JUoW:
    """Unit of Work converts a GrapDocumentModel into equivalent Cypher queries"""

    def __init__(self, document: Document) -> None:
        self.model = GraphModel(document)

    @property
    def node_id(self):
        return self.model.dataobj.uid

    @property
    def _node_match_props(self) -> str:
        """cypher MATCH query for matching the node with this.node_id"""
        return no_quotes_object({"uid": self.node_id})

    @property
    def _node_properties(self) -> str:
        """Unpacking model's attribs into Cypher's node property syntax"""
        props = {
            "uid": self.node_id,  # custom node id
            "contents": _escape_double_quote(self.model.dataobj.contents),
            **self.model.dataobj.fields,  # other optional documents metadata
        }
        props = invalid_key_fix(props, invalid_sym="-", valid_sym="_")
        return no_quotes_object(props)

    @property
    def node_label(self) -> str:
        return self.model.dict["entity_type"].capitalize()

    def detach_all_relationships(self, tx):
        q = f"MATCH (n {self._node_match_props})-[r:LINK]->() DELETE r"
        tx.run(q)

    def create_dep_nodes(self, tx, rel_ids):
        for link_id in rel_ids:
            q = f"MERGE (n {no_quotes_object({'id': link_id})})"
            tx.run(q)

    def create_one_to_many_rel(self, tx, rel_ids):
        existing_nodes_query = f"""
        MATCH ( n {self._node_match_props} )
        MATCH (target) WHERE target.id IN {rel_ids}
        MERGE (n)-[:LINK]->(target)
        """
        tx.run(existing_nodes_query)


@DocToDBAdapters.register(name="neo4j")
class Neo4JUoW(_Neo4JUoW, DocumentToDB):
    def update_or_create_document(self, tx):
        """Create or update a node in Neo4J

        This includes:
        1. Merge with the Node with the same Node.id
        2. Set the Node's label as entity_type
        3. Set the Node's properties with new properties
        4. Set the Node's lastEdited properties with updated timestamp

        """

        query = f"""
        MERGE ( n {self._node_match_props} )
        SET 
            n:{self.node_label},
            n = {self._node_properties},
            n.lastEdited = timestamp()         
        """

        logger.debug("neo4j - updating or creating new document")
        logger.debug("query:\n%s", query)

        tx.run(query)

    def update_or_create_relationships(self, tx):
        relationships = self.model.dict["relations"]

        self.detach_all_relationships(tx)

        if not relationships:
            return

        self.create_dep_nodes(tx, list(relationships))
        self.create_one_to_many_rel(tx, list(relationships))

    def delete_document(self, *args, **kwargs) -> bool:
        return
