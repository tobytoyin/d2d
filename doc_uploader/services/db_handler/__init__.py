# from doc_uploader.connectors.factory import ConnectorFactory

# from ...app.profile import Profile

# # from doc_uploader.services.db_handler.


# class Uploader:
#     def __init__(self, profile: Profile = Profile()) -> None:
#         self.profile = profile

#     def mock_uploader(self, doc_model):
#         conn = ConnectorFactory(profile=self.profile).mock
#         uow = UoWFactory(doc_model=doc_model).mock

#         fields_count = conn.run(uow.update_or_create_document)
#         relations_count = conn.run(uow.update_or_create_relationships)
#         return fields_count, relations_count

#     # def neo4j_uploader(self, doc_model):
#     #     conn = ConnectorFactory(profile=self.profile).neo4j  # get connector
#     #     uow = UoWFactory(doc_model=doc_model).neo4j

#     #     conn.run(uow.update_or_create_node)
#     #     conn.run(uow.update_or_create_relationships)
