from functools import cached_property

from doc_uploader.contracts.document import (
    Document,
    DocumentContent,
    DocumentMetadata,
    DocumentRelations,
)
from doc_uploader.contracts.source import Source

from ._processor import frontmatter_processor, links_processor


class ObsidianAdapter:
    @classmethod
    def create_document(cls, source: Source) -> Document:
        uid = str(source.path).split("/")[-1].split(".")[0]

        with open(source.path, "r") as f:
            text = f.read()
            content = DocumentContent(contents=text, bytes=text.encode())

        return Document(
            uid=uid,
            source=source,
            content=content,
            metadata=cls._create_metadata(text),
            relations=cls._create_links(text),
        )

    @classmethod
    def _create_metadata(cls, text):
        metadata: dict = frontmatter_processor(text)
        return DocumentMetadata(**metadata)

    @classmethod
    def _create_links(cls, text):
        out = []
        links = links_processor(text)
        for link in links:
            doc_id = link.pop("rel_uid")
            rel_type = link.pop("rel_type")
            new_obj = {"rel_uid": doc_id, "rel_type": rel_type, "properties": link}
            out += [DocumentRelations(**new_obj)]

        return set(out)
