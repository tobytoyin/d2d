import uuid

from doc_uploader.contracts.document import Document, DocumentContent
from doc_uploader.contracts.source import Source


class MockAdapter:
    @staticmethod
    def create_document(source: Source) -> Document:
        uid = str(uuid.uuid4())

        content = DocumentContent(
            contents="hello world",
            bytes="hellow world".encode(),
        )

        return Document(uid=uid, source=source, content=content)
