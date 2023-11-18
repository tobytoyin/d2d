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
        self._driver_instance = None

    def set_creds(self, **kwargs):
        self._driver_instance = None  # reset driver
        for k, v in kwargs.items():
            self.creds[k.lower()] = v

    def create_driver(self):
        if not all(x is not None for x in self.creds.values()):
            raise AttributeError

        uri = self.creds["uri"]
        user = self.creds["user"]
        pwd = self.creds["password"]

        self._driver_instance = GraphDatabase.driver(uri, auth=(user, pwd))  # type: ignore
        logging.info(f"driver@{uri} has initialsied....")
        return self._driver_instance

    @property
    def driver(self):
        if self._driver_instance:
            return self._driver_instance

        return self.create_driver()

    def close_driver(self):
        if self._driver_instance:
            self._driver_instance.close()
