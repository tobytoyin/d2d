from pathlib import Path

from d2d.contracts.document import (
    DocContent,
    DocMetadata,
    DocRelation,
    Document,
    Source,
)


def create_document_runtime(uid, doc_type, contents, relations, **fields):
    return Document(
        uid=uid,
        content=DocContent(contents=contents, bytes=contents.encode()),
        source=Source(path=Path("."), source_type="runtime"),
        metadata=DocMetadata(doc_type=doc_type, properties=fields),
        relations=set([DocRelation(**rel) for rel in relations]),
    )
