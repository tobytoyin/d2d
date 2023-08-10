from neo4j import GraphDatabase


class Neo4JConnector:
    def __init__(self, uri, username, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        
    # def __enter__(self):
    #     session = 
    #     self.session = session
    #     return self.session

    # def __exit__(self, exc_type, exc_value, exc_tb):
    #     # methods that could exec in finally block
    #     self.session.close()
    #     return True
