from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Set, TypeAlias

from pydantic import BaseModel

from .source import Source


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    ...


class DocumentContent(DocumentComponent):
    contents: str
    bytes: bytes

    def __hash__(self) -> int:
        return hash(self.bytes)


class DocUID(str, DocumentComponent):
    ...


class DocumentSummary(str, DocumentComponent):
    ...


class DocumentKeywords(Set, DocumentComponent):
    ...


class DocumentMetadata(BaseModel):
    """A Struct for the metadata in a document

    `DocMetadata` represents a set of key-value pair which:
    - doc_type (required field)
    - extra keys
    """

    doc_type: str = "document"  # required field
    properties: Dict[str, Any] = {}


class DocumentRelation(BaseModel):
    rel_uid: DocUID
    rel_type: str
    properties: Dict[str, Any] = {}

    def __hash__(self) -> int:
        # return the hash of an immutable dictionary
        return frozenset(self.model_dump()).__hash__()


class DocumentRelations(
    Set[DocumentRelation],
    DocumentComponent,
):
    ...


class Document(BaseModel):
    uid: DocUID
    source: Source
    content: DocumentContent
    metadata: DocumentMetadata = DocumentMetadata()
    relations: DocumentRelations = DocumentRelations()

    # optional fields
    summary: DocumentSummary = DocumentSummary()
    keywords: DocumentKeywords = DocumentKeywords()
