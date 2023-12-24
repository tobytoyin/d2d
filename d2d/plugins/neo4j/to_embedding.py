# from d2d.contracts.documents import Document

# from ..document_to_db import _NodeIdentity
# from ..interface import DocumentPlugin
# from .mixin import GraphDBMixin
# from .utils import no_quotes_object

# # class DocumentToN4JEmbedding(DocumentPlugin, GraphDBMixin):
# #     def update_or_create_embedding(self, document: Document):
# #         match_self = _NodeIdentity.get_self(document)
# #         embedding = no_quotes_object(document.embedding.prefix_model_dump())

# #         new_props = {f"root.{k} = {v}" for k, v in embedding.items()}
# #         query = f"""
# #         WITH apoc.convert.fromJsonMap({repr(json_props)}) AS props
# #         MERGE ( n {match_self} )
# #         SET
# #             n = props,
# #             n:{_NodeIdentity.node_label(document)},
# #             n.lastEdited = timestamp()
# #         """
# #         print(query)
# #         tx = lambda tx: tx.run(query)

# #         with self.driver.session() as session:
# #             _ = session.execute_write(tx)
# #         self.close_driver()
