import uuid
from typing import Set

from doc_uploader.doc_processor.factory import DocumentAdapterContainer
from doc_uploader.doc_processor.interfaces import DocumentAdapter
from doc_uploader.doc_processor.types import DocID, MetadataKVPair, NormalisedContents


@DocumentAdapterContainer.register(name="mock")
class MockAdapter(DocumentAdapter):
    """This Adapter just generate a random document

    Args:
        DocumentAdapter (_type_): _description_
    """

    def __init__(self, skip_) -> None:
        pass

    def id_processor(self) -> DocID:
        return str(uuid.uuid1())

    def metadata_processor(self) -> MetadataKVPair:
        return {"doc_type": "test"}

    def relations_processor(self):
        return [
            {"rel_uid": str(uuid.uuid1()), "rel_type": "LINK"},
            {"rel_uid": str(uuid.uuid1()), "rel_type": "LINK"},
        ]

    def contents_normaliser(self):
        return "normalised hello world"
