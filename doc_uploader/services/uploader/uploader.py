from doc_uploader.connectors.factory import ConnectorFactory, UoWFactory

from ...app.profile import Profile


class Uploader:
    def __init__(self, profile: Profile) -> None:
        self.profile = profile

    def neo4j_uploader(self, doc_model):
        conn = ConnectorFactory(profile=self.profile).neo4j
        uow = UoWFactory(doc_model=doc_model).neo4j

        conn.run(uow.update_or_create_node)
        conn.run(uow.update_or_create_relationships)
