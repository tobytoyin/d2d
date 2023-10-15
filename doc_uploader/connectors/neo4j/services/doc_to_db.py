import logging
from typing import Set

from doc_uploader.doc_processor.interfaces import Document, RelationProps
from doc_uploader.models.factory import create_graph_model
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
        self.model = create_graph_model(document)

    @property
    def node_id(self):
        return self.model.uid

    @property
    def _node_match_props(self) -> str:
        """cypher MATCH query for matching the node with this.node_id"""
        return no_quotes_object({"uid": self.node_id})

    @property
    def _node_properties(self) -> str:
        """Unpacking model's attribs into Cypher's node property syntax"""
        props = {
            "uid": self.node_id,  # custom node id
            "contents": _escape_double_quote(self.model.contents),
            **self.model.fields,  # other optional documents metadata
        }
        props = invalid_key_fix(props, invalid_sym="-", valid_sym="_")
        return no_quotes_object(props)

    @property
    def node_label(self) -> str:
        return self.model.node_type.capitalize()

    def detach_all_relationships(self, tx):
        q = f"MATCH (n {self._node_match_props})-[r]->() DELETE r"
        tx.run(q)

    def create_dep_nodes(self, tx, relations: Set[RelationProps]):
        for link in relations:
            q = f"MERGE (n {no_quotes_object({'uid': link.rel_uid})})"
            tx.run(q)

    def create_one_to_many_rel(self, tx, relations: Set[RelationProps]):
        match_root_query = f"MATCH ( n {self._node_match_props} )"
        match_rels_queries = []
        merge_rels_queries = []

        for idx, rel in enumerate(relations):
            link_props = no_quotes_object(rel.properties)
            rel_node_id = no_quotes_object({"uid": rel.rel_uid})

            match_q = f"MATCH (target{idx} {rel_node_id})"
            merge_q = f"MERGE (n)-[ :{rel.rel_type} {link_props} ]->(target{idx})"

            match_rels_queries.append(match_q)
            merge_rels_queries.append(merge_q)

        relations_match_q = "\n".join(match_rels_queries)
        relations_merge_q = "\n".join(merge_rels_queries)

        final_query = f"""
        {match_root_query}
        {relations_match_q}
        {relations_merge_q}
        """
        print(final_query)
        tx.run(final_query)


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
        relationships = self.model.relations

        self.detach_all_relationships(tx)

        if not relationships:
            return

        self.create_dep_nodes(tx, relationships)
        self.create_one_to_many_rel(tx, relationships)

    def delete_document(self, *args, **kwargs) -> bool:
        return