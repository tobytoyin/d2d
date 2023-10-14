from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeAlias

from pydantic import BaseModel

from ..source import ObjectSource

DocUID: TypeAlias = str


class Document(BaseModel):
    uid: DocUID
    source: ObjectSource
    content: DocumentContent


class DocumentContent(BaseModel):
    contents: str
    bytes: bytes

    def __hash__(self) -> int:
        return hash(self.bytes)
