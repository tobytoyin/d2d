import uuid

from d2d.contracts.document import DocContent, Document
from d2d.contracts.source import Source


class MockAdapter:
    @staticmethod
    def create_document(source: Source) -> Document:
        uid = str(uuid.uuid4())

        content = DocContent(
            contents="hello world",
            bytes="hellow world".encode(),
        )

        return Document(uid=uid, source=source, content=content)
