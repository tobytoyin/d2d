from abc import abstractmethod
from typing import Callable, Set

from pydantic import BaseModel, ConfigDict

RelationsProcessorFn = Callable[[str], set]
MetadataProcessorFn = Callable[[str], dict]


class DocumentMetadata(BaseModel):
    """Class to convert dict int a Metadataclass"""

    model_config = ConfigDict(extra='allow')
    doc_type: str


class Document(BaseModel):
    relations_processor: RelationsProcessorFn = None
    metadata_processor: MetadataProcessorFn = None

    _contents: str = None  # str contents of the document
    _id: str = None
    _metadata: DocumentMetadata = None
    _relations: Set[str] = None

    path: str  # source path of the document

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
        if not self._contents:
            self._contents = self.read()

        return self._contents

    @property
    def id(self):
        if not self._id:
            self._id = self.id_resolver()

        return self._id

    @property
    def metadata(self):
        """Return the metadata of a Document"""
        if self._metadata:
            return self._metadata

        metadata = self.metadata_processor(self.contents)
        self._metadata = DocumentMetadata(**metadata)
        return self._metadata

    @property
    def relations(self):
        """use the `relations_processor` function to extract Relationship ID in doc"""
        if self._relations:
            return self._relations

        if self.relations_processor:
            self._relations = self.relations_processor(self.contents)
            
        return self._relations


