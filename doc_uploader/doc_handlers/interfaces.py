from abc import abstractmethod
from typing import Any, Dict, Iterable, Optional, Protocol, Set, runtime_checkable

from pydantic import BaseModel

from .types import DocID, MetadataKVPair, NormalisedContents


class MetadataProps(BaseModel):
    """A Struct for the metadata in a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    doc_type: str = "document"  # required field
    properties: Dict[str, Any] = {}


class RelationProps(BaseModel):
    rel_uid: DocID
    rel_type: str
    properties: Optional[Dict[str, Any]] = {}

    def __hash__(self) -> int:
        # return the hash of an immutable dictionary
        return frozenset(self.model_dump()).__hash__()


class Document(BaseModel):
    """Final datamodel to represent a Document

    This provides a structure to create the

    Args:
        BaseModel (_type_): _description_
    """

    uid: DocID
    metadata: MetadataProps
    relations: Set[RelationProps]
    contents: NormalisedContents


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
    def uid(self) -> DocID:
        return self.adapter.id_processor()

    @property
    def metadata(self) -> MetadataProps:
        """Returns the metadata of a document as a key-value pair map

        Returns:
            DocMetadata: struct for a valid document's metadata
        """
        metadata_map = self.adapter.metadata_processor()
        return MetadataProps(**metadata_map)

    @property
    def relations(self) -> Set[RelationProps]:
        relations_props = self.adapter.relations_processor()
        iter_props = (RelationProps(**prop) for prop in relations_props)
        return set(iter_props)

    @property
    def contents(self) -> NormalisedContents:
        return self.adapter.contents_normaliser()
