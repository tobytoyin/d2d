from typing import Set

from doc_uploader.doc_handlers.factory import Registry
from doc_uploader.doc_handlers.interfaces import DocumentAdapter
from doc_uploader.doc_handlers.types import DocID, MetadataKVPair, NormalisedContents

from .processors import frontmatter_processor, links_processor


@Registry.register(name="obsidian")
class ObsidianAdapter(DocumentAdapter):
    def __init__(self, text: str, **kwargs) -> None:
        super().__init__(text, **kwargs)
        self.path = kwargs["path"]

    def id_processor(self) -> DocID:
        return self.path.split("/")[-1].split(".")[0]

    def metadata_processor(self) -> MetadataKVPair:
        return frontmatter_processor(self.text)

    def relations_processor(self) -> Set[DocID]:
        return links_processor(self.text)

    def contents_normaliser(self) -> NormalisedContents:
        return self.text
