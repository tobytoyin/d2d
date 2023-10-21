from pathlib import Path

from d2d.contracts.document import (
    Document,
    DocumentContent,
    DocumentMetadata,
    DocumentRelations,
    Source,
)


def create_document_runtime(uid, doc_type, contents, relations, **fields):
    return Document(
        uid=uid,
        content=DocumentContent(contents=contents, bytes=contents.encode()),
        source=Source(path=Path("."), source_type="runtime"),
        metadata=DocumentMetadata(doc_type=doc_type, properties=fields),
        relations=set([DocumentRelations(**rel) for rel in relations]),
    )
