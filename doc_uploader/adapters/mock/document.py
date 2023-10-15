import uuid

from doc_uploader.contracts.document import Document, DocumentContent
from doc_uploader.contracts.source import Source


class MockAdapter:
    @classmethod
    def create_document(cls, source: Source) -> Document:
        uid = str(uuid.uuid1())

        content = DocumentContent(
            contents="hello world",
            bytes="hellow world".encode(),
        )

        return Document(uid=uid, source=source, content=content)
