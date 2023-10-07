import logging

from ...factory import DocToDBAdapters
from ...protocols import DocumentToDB

# @DocToDBAdapters.register(name="mock")
# class MockHandler(DocumentToDB):
#     def __init__(self, model: BaseDBModel) -> None:
#         self.model = model
#         super().__init__()

#     def update_or_create_document(self):
#         logging.debug(self.model.dataobj)
#         logging.debug("updated and created document")
#         return len(self.model.dict.keys())

#     def update_or_create_relationships(self):
#         logging.debug(f"created relationships: {self.model.dataobj.relations}")
#         return len(self.model.dataobj.relations)
