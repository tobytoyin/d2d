from ..base import BaseDocument, DocMetadata


class FakeDocument(BaseDocument):
    def read(self) -> str:
        return ""

    def id_resolver(self) -> str:
        return self.id


def mock_creator(content: str, id: str, relations: set, doc_type: str, **metadata):
    metadata = DocMetadata(doc_type=doc_type, **metadata)
    doc = FakeDocument(
        path="",
        contents_=content,
        id_=id,
        metadata_=metadata,
        relations_=relations,
    )
    return doc
