from typing import Protocol

from doc_uploader.contracts.document import Document


class DocumentService(Protocol):
    document: Document
