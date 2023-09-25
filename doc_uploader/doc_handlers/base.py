from abc import ABC, abstractmethod
from typing import Callable, Optional, Set

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
    relations_: Optional[Set[str]] = None

    metadata_processor: MetadataProcessorFn = None
    relations_processor: RelationsProcessorFn = None
    contents_normaliser: ContentsNormaliserFn = None

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
    def metadata(self):
        """Return the metadata of a Document"""
        print(self.metadata_)
        if self.metadata_:
            return self.metadata_.model_dump()

        metadata = self.metadata_processor(self.contents)
        self._metadata_in = DocMetadata(**metadata)
        return self._metadata_in.model_dump()

    @property
    def relations(self):
        """use the `relations_processor` function to extract Relationship ID in doc"""
        if self.relations_:
            return self.relations_

        if self.relations_processor:
            self.relations_ = self.relations_processor(self.contents)

        return self.relations_
