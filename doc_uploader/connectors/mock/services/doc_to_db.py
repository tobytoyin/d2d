import logging

from doc_uploader.contracts.document import Document


class MockHandler:
    def __init__(self, document: Document) -> None:
        self.document = document

    def update_or_create_document(self):
        return 1

    def update_or_create_relationships(self):
        return len(self.document.relations)
