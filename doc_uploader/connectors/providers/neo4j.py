import logging

from neo4j import GraphDatabase

from ..factory import ConnectorsContainer


@ConnectorsContainer.register(name="neo4j")
class Neo4JConnector:
    def __init__(self, uri, username, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def run(self, uow):
        with self.driver.session() as session:
            result = session.execute_write(uow)
            logging.debug(f"neo4j result {result}")

        self.close()
