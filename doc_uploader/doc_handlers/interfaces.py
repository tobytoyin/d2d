from abc import abstractmethod
from typing import Any, Dict, Iterable, Optional, Protocol, Set, runtime_checkable

from pydantic import BaseModel, ConfigDict

from .types import DocID, MetadataKVPair, NormalisedContents


class DocMetadata(BaseModel):
    """A Struct for the metadata in a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    model_config = ConfigDict(extra="allow")
    doc_type: str = "document"  # required field


class DocRelations(BaseModel):
    doc_id: DocID
    rel_type: str
    properties: Optional[Dict[str, Any]] = {}
    # other extra fields all relational properties

    def __hash__(self) -> int:
        # return the hash of an immutable dictionary
        return frozenset(self.model_dump()).__hash__()


class Document(BaseModel):
    """Final datamodel to represent a Document

    Args:
        BaseModel (_type_): _description_
    """

    uid: DocID
    contents: NormalisedContents
    metadata: DocMetadata
    relations: Set[DocRelations]


@runtime_checkable
class DocumentAdapter(Protocol):
    @abstractmethod
    def id_processor(self) -> DocID:
        """Method to define how Document ID should be created"""
        ...

    @abstractmethod
    def metadata_processor(self) -> MetadataKVPair:
        """_summary_

        Returns:
            MetadataKVPair: \
                dictionary object (limits to certain types in value), \
                see `types.MetadataKVPair`.
        """
        ...

    @abstractmethod
    def relations_processor(self) -> Iterable[dict]:
        """_summary_

        Returns:
            Set[DocRelations]: \
                returns an Iterable dictionarys containing \
                relational properties
        """
        ...

    @abstractmethod
    def contents_normaliser(self) -> NormalisedContents:
        ...


class DocumentProps:
    """DocumentProps uses an DocumentAdapter as an Interface to:
    - extract relations via `self.relations`
    - extract metadata  via `self.metadata`

    Each of the property invoke the implemented method within DocumentAdapter
    """

    def __init__(self, doc_adapter: DocumentAdapter) -> None:
        self.adapter = doc_adapter

    @property
    def id(self) -> DocID:
        return self.adapter.id_processor()

    @property
    def metadata(self) -> DocMetadata:
        """Returns the metadata of a document as a key-value pair map

        Returns:
            DocMetadata: struct for a valid document's metadata
        """
        metadata_map = self.adapter.metadata_processor()
        return DocMetadata(**metadata_map)

    @property
    def relations(self) -> Set[DocRelations]:
        relations_props = self.adapter.relations_processor()
        iter_props = (DocRelations(**prop) for prop in relations_props)
        return set(iter_props)

    @property
    def contents(self) -> NormalisedContents:
        return self.adapter.contents_normaliser()
        return self.adapter.contents_normaliser()
        return self.adapter.contents_normaliser()
