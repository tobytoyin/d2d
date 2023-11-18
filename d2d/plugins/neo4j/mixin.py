import logging
import os

from neo4j import GraphDatabase


class GraphDBMixin:
    def __init__(self) -> None:
        self.creds = {
            "uri": os.environ.get("NEO4J_URI"),
            "password": os.environ.get("NEO4J_PASSWORD"),
            "user": os.environ.get("NEO4J_USER"),
        }
        self.driver = None

    def set_creds(self, **kwargs):
        self.driver = None  # reset driver
        for k, v in kwargs.items():
            self.creds[k.lower()] = v

    def get_driver(self):
        if self.driver:
            return self.driver

        if not all(x is not None for x in self.creds.values()):
            raise AttributeError

        uri = self.creds["uri"]
        user = self.creds["user"]
        pwd = self.creds["password"]

        self.driver = GraphDatabase.driver(uri, auth=(user, pwd))  # type: ignore
        logging.info(f"driver@{uri} has initialsied....")
        return self.driver

    def close(self):
        if self.driver:
            self.driver.close()
