from abc import ABC, abstractmethod
from typing import Any, Callable, Optional, Set

from pydantic import BaseModel, ConfigDict

RelationsProcessorFn = Callable[[str], set]
MetadataProcessorFn = Callable[[str], dict]
ContentsNormaliserFn = Callable[[str], str]


class DocMetadata(BaseModel):
    """Class representing the metadata of a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    model_config = ConfigDict(extra="allow")
    # required fields
    doc_type: str


class BaseDocument(ABC, BaseModel):
    path: str  # source path of the document

    # optional fields when construct directly within read from file
    contents_: Optional[str] = None  # str contents of the document
    id_: Optional[str] = None
    metadata_: Optional[DocMetadata] = None
    relations_: Set[str] = set()

    metadata_processor: MetadataProcessorFn = lambda _: {}
    relations_processor: RelationsProcessorFn = lambda _: set()
    contents_normaliser: ContentsNormaliserFn = lambda _: ""

    def model_post_init(self, __context: Any) -> None:
        self._parse_metadata()
        self._parse_relations()
        return super().model_post_init(__context)

    @abstractmethod
    def read(self) -> str:
        ...

    @abstractmethod
    def id_resolver(self) -> str:
        """Method to define how Document ID should be created"""
        ...

    @property
    def contents(self) -> str:
        """Return the text contents of a Document"""
        if not self.contents_:
            self.contents_ = self.read()

        return self.contents_

    @property
    def id(self):
        if not self.id_:
            self.id_ = self.id_resolver()

        return self.id_

    @property
    def entity_type(self):
        return self.metadata_.model_dump().get("doc_type")

    def _parse_metadata(self):
        if self.metadata_:
            return

        metadata = self.metadata_processor(self.contents)
        self.metadata_ = DocMetadata(**metadata)

    def _parse_relations(self):
        if self.relations_:
            return

        if self.relations_processor:
            self.relations_ = self.relations_processor(self.contents)

    @property
    def metadata(self):
        """Return the metadata of a Document"""
        metadata = self.metadata_.model_dump()
        metadata.pop("doc_type")
        return metadata

    @property
    def relations(self):
        """use the `relations_processor` function to extract Relationship ID in doc"""
        return self.relations_
