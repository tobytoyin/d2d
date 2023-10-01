import logging
import os

from neo4j import GraphDatabase

from ..factory import ConnectorsContainer


@ConnectorsContainer.register(name="neo4j")
class Neo4JConnector:
    def __init__(self) -> None:
        uri = os.environ.get("NEO4J_URI")
        print(uri)
        username = os.environ.get("NEO4J_USER")
        password = os.environ.get("NEO4J_PW")
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def run(self, uow):
        with self.driver.session() as session:
            result = session.execute_write(uow)
            logging.debug(f"neo4j result {result}")

        self.close()
