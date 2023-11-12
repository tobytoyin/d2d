from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, TypeAlias

from pydantic import BaseModel

SourcePayloadDict: TypeAlias = dict[str, str]


class Source(BaseModel):
    path: Path
    options: Optional[dict[str, str]] = {}

    def __hash__(self):
        return hash(self.path)


class SourceReader(BaseModel):
    provider: str
    options: Optional[dict[str, str]] = {}


class TaskPayload(BaseModel):
    provider: str
    options: Optional[dict[str, str]] = {}


class SourcePayload(BaseModel):
    source: Source
    source_reader: SourceReader
    tasks: dict[str, TaskPayload]


class TaskFunctionResult(BaseModel):
    result: Any
    kind: str
