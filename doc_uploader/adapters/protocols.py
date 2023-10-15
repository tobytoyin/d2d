from typing import Protocol

from doc_uploader.contracts.document import Document


class DocumentAdapter(Protocol):
    def create_document(self) -> Document:
        ...
