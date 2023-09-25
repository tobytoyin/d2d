import yaml
from base.db_models import GraphDocumentModel
from neo4j import GraphDatabase
from utils import no_quotes_object


class Neo4JUoW:
    """Unit of Work converts a GrapDocumentModel into equivalent Cypher queries"""
    def __init__(self, model: GraphDocumentModel) -> None:
        self.model = model
        self.doc_id = self.model.record['id']

    @property
    def node_match_props(self) -> str:
        return no_quotes_object({'id': self.doc_id})

    @property
    def node_props(self) -> str:
        obj = {'id': self.doc_id, **self.model.record['fields']}
        return no_quotes_object(obj)

    @property
    def node_label(self) -> str:
        return self.model.record['node_type'].capitalize()

    def update_or_create_node(self, tx):
        """create or update a node"""

        query = f"""
        MERGE (n {self.node_match_props})
        SET 
            n:{self.node_label},
            n = {self.node_props},
            n.lastEdited = timestamp()         
        """

        print(query)
        tx.run(query)

    
    def detach_all_relationships(self, tx):
        q = f"MATCH (n {self.node_match_props})-[r:LINK]->() DELETE r"
        tx.run(q)    
        
        
    def create_dep_nodes(self, tx, rel_ids):
       for link_id in rel_ids:
            q = f"MERGE (n {no_quotes_object({'id': link_id})})"
            print(q)
            tx.run(q)        
            

    def create_one_to_many_rel(self, tx, rel_ids):
        existing_nodes_query = f"""
        MATCH (n {self.node_match_props})
        MATCH (target) WHERE target.id IN {rel_ids}
        MERGE (n)-[:LINK]->(target)
        """
        print(existing_nodes_query)
        tx.run(existing_nodes_query)              


    def update_or_create_relationships(self, tx):
        relationships = self.model.record['relations']
        
        self.detach_all_relationships(tx)

        if not relationships:
            return

        self.create_dep_nodes(tx, list(relationships))
        self.create_one_to_many_rel(tx, list(relationships))



class Neo4JConnector:
    def __init__(self, uri, username, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def run(self, uow):
        with self.driver.session() as session:
            result = session.execute_write(uow)

        self.close()

    # def __enter__(self):
    #     session =
    #     self.session = session
    #     return self.session

    # def __exit__(self, exc_type, exc_value, exc_tb):
    #     # methods that could exec in finally block
    #     self.session.close()
    #     return True
