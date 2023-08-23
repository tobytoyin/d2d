import yaml
from base.db_models import GraphDocumentModel
from neo4j import GraphDatabase
from utils import no_quotes_object


class Neo4JGraphModelAdapter:
    def __init__(self, model: GraphDocumentModel) -> None:
        self.model = model
        self.doc_id = "222"

    @property
    def node_match(self) -> str:
        return no_quotes_object({'id': self.doc_id})
    
        
    @property
    def node_properties(self) -> str:     
        obj = {'id': self.doc_id, **self.model.record['fields']}
        return no_quotes_object(obj)
    
    @property
    def node_label(self) -> str:
        return self.model.record['node_type'].capitalize()
        
    def update_or_create_node(self, tx):
        """create or update a node"""
        query = f"""
            OPTIONAL MATCH (n {self.node_match})
            SET n = {self.node_properties} 
            SET n:{self.node_label}
            
            WITH n
            WHERE n IS NULL
            MERGE (:{self.node_label} {self.node_properties})
        """
        print(query)
        result = tx.run(query)
        
    def create_relations_work(self, tx):
        relationships = self.model.record['relations']
        queries = [f"MATCH (n {no_quotes_object({'id': self.doc_id})})"]
        
        if not relationships: 
            return 
        
        for link_id in relationships:
            queries.append(f"MERGE (n)-[:link]->({no_quotes_object({'id': link_id})})")
            
        query = ' '.join(queries)
        print(query)
        result = tx.run(query)


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
