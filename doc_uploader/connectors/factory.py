from ..app.profile import Profile
from .mock import MockConnector
from .neo4j import Neo4JConnector


class ConnectorFactory:
    def __init__(self, profile: Profile) -> None:
        self.profile = profile

    @property
    def mock(self):
        return MockConnector()

    @property
    def neo4j(self):
        cred = self.profile.storage("neo4j")

        return Neo4JConnector(
            uri=cred["uri"],
            username=cred["username"],
            password=cred["password"],
        )
