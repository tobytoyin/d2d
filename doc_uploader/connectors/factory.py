from doc_uploader.app.profile import Profile
from doc_uploader.common.factory import FactoryRegistry


class ConnectorsContainer(FactoryRegistry):
    _map = {}
    import_pattern = "doc_uploader/connectors/providers/*.py"


def get_profile(connector_name: str):
    profile = Profile()
    return profile.storage(connector_name)


def get_connector(name: str, *args, **kwargs):
    connector = ConnectorsContainer.get(name=name)
    profile = get_profile(name)
    return connector(**profile)


# class ConnectorFactory:
#     def __init__(self, profile: Profile) -> None:
#         self.profile = profile

#     @property
#     def mock(self):
#         return MockConnector()

#     @property
#     def neo4j(self):
#         cred = self.profile.storage("neo4j")

#         return Neo4JConnector(
#             uri=cred["uri"],
#             username=cred["username"],
#             password=cred["password"],
#         )
