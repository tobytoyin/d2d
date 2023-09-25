import .neo4j as neo4j
from ..app.profile import Profile


class ConnectorFactory:
    def __init__(self, profile: Profile) -> None:
        self.profile = profile

    @property
    def neo4j(self):
        cred = self.profile.storage('neo4j')

        return neo4j.Neo4JConnector(
            uri=cred['uri'],
            username=cred['username'],
            password=cred['password'],
        )


