import yaml
from base.db_models import GraphDocumentModel
from neo4j import GraphDatabase


class Neo4JGraphModelAdapter:
    def __init__(self, model: GraphDocumentModel) -> None:
        self.model = model
        
    @property
    def node_properties(self) -> str: 
        prop_strings = []
        for k, v in self.model.record['fields'].items():
            prop_strings.append(f'{k}: "{v}"')
            
        prop_strings.append(f"id: '{self.model.record['id']}'")
        return '{' + ','.join(prop_strings) + '}'
    
    @property
    def node_label(self) -> str:
        return self.model.record['node_type'].capitalize()
        
    def create_node_work(self, tx):
        query = f"""
            CREATE (
                n: {self.node_label}
                {self.node_properties}
            )
        """
        print(query)
        result = tx.run(query)
        result.consume()
        
    def create_relations_work(self, tx):
        ...


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
