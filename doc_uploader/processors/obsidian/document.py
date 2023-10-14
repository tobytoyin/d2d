from functools import cached_property

from doc_uploader.contracts.document import Document, DocumentContent
from doc_uploader.contracts.source import ObjectSource


class ObsidianAdapter:
    @classmethod
    def create_document(cls, source: ObjectSource) -> Document:
        uid = str(source.path).split("/")[-1].split(".")[0]

        with open(source.path, "r") as f:
            text = f.read()
            content = DocumentContent(contents=text, bytes=text.encode())

        return Document(uid=uid, source=source, content=content)
