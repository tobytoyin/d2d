from doc_uploader.models.datamodels import GraphModel
from doc_uploader.utils import no_quotes_object

from ...factory import DocToDBAdapters
from ...protocols import DocumentToDB


class _Neo4JUoW:
    """Unit of Work converts a GrapDocumentModel into equivalent Cypher queries"""

    def __init__(self, model: GraphModel) -> None:
        self.model = model
        self.doc_id = self.model.dict["id"]

    @property
    def _node_match_props(self) -> str:
        return no_quotes_object({"id": self.doc_id})

    @property
    def _node_props(self) -> str:
        obj = {"id": self.doc_id, **self.model.dict["fields"]}
        return no_quotes_object(obj)

    @property
    def node_label(self) -> str:
        return self.model.dict["node_type"].capitalize()

    def detach_all_relationships(self, tx):
        q = f"MATCH (n {self._node_match_props})-[r:LINK]->() DELETE r"
        tx.run(q)

    def create_dep_nodes(self, tx, rel_ids):
        for link_id in rel_ids:
            q = f"MERGE (n {no_quotes_object({'id': link_id})})"
            print(q)
            tx.run(q)

    def create_one_to_many_rel(self, tx, rel_ids):
        existing_nodes_query = f"""
        MATCH (n {self._node_match_props})
        MATCH (target) WHERE target.id IN {rel_ids}
        MERGE (n)-[:LINK]->(target)
        """
        print(existing_nodes_query)
        tx.run(existing_nodes_query)


@DocToDBAdapters.register(name="neo4j")
class Neo4JUoW(_Neo4JUoW, DocumentToDB):
    def update_or_create_document(self, tx):
        """create or update a node"""

        query = f"""
        MERGE (n {self._node_match_props})
        SET 
            n:{self.node_label},
            n = {self._node_props},
            n.lastEdited = timestamp()         
        """

        print(query)
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
