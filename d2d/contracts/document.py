from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, Sequence, Type, TypeAlias

from pydantic import BaseModel, ConfigDict

from .source import Source

CompatibleDictValues: TypeAlias = str | list | int | float


class DocumentComponent:
    """Type of components that compose a `Document`"""

    ...


class DocContent(DocumentComponent, BaseModel):
    contents: str
    bytes: bytes

    def __hash__(self) -> int:
        return hash(self.bytes)


class DocUID(str, DocumentComponent):
    ...


class DocSummary(str, DocumentComponent):
    ...


class DocKeywords(set, DocumentComponent):
    ...


class DocMetadata(BaseModel, DocumentComponent):
    """A Struct for the metadata in a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    doc_type: str = "document"  # required field
    properties: Dict[str, CompatibleDictValues] = {}


class DocRelation(BaseModel, DocumentComponent):
    rel_uid: DocUID
    rel_type: str
    properties: Dict[str, CompatibleDictValues] = {}

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __hash__(self) -> int:
        # return the hash of an immutable dictionary
        return frozenset(self.model_dump()).__hash__()


class DocRelations(set[DocRelation], DocumentComponent):
    def __new__(cls, /, doc_relations=None):
        if not doc_relations:
            return set()

        cls._check_input_type(doc_relations)
        return super().__new__(cls)

    # check input types
    @classmethod
    def _check_input_type(cls, arg):
        if not isinstance(arg, Iterable):
            raise TypeError("input is not of a Iterable type")

        for el in arg:
            cls._check_element(el)

    @classmethod
    def _check_element(cls, element):
        if not isinstance(element, DocRelation):
            raise TypeError("input element is not a DocRelation type")


class Document(BaseModel):
    source: Source
    uid: DocUID
    content: DocContent

    # optional fields
    metadata: DocMetadata = DocMetadata()
    relations: DocRelations = DocRelations()
    summary: DocSummary = DocSummary()
    keywords: DocKeywords = DocKeywords()

    model_config = ConfigDict(arbitrary_types_allowed=True)
