from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Set, TypeAlias

from pydantic import BaseModel

from .source import Source

DocUID: TypeAlias = str


class DocumentContent(BaseModel):
    contents: str
    bytes: bytes

    def __hash__(self) -> int:
        return hash(self.bytes)


class DocumentMetadata(BaseModel):
    """A Struct for the metadata in a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    doc_type: str = "document"  # required field
    properties: Dict[str, Any] = {}


class DocumentRelations(BaseModel):
    rel_uid: DocUID
    rel_type: str
    properties: Dict[str, Any] = {}

    def __hash__(self) -> int:
        # return the hash of an immutable dictionary
        return frozenset(self.model_dump()).__hash__()


class Document(BaseModel):
    uid: DocUID
    source: Source
    content: DocumentContent
    metadata: DocumentMetadata = DocumentMetadata()
    relations: Set[DocumentRelations] = set()
