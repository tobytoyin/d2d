from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, TypeAlias

from pydantic import BaseModel


class Options(BaseModel):
    mapping: dict[str, Any] | None = None  # the kwarg-value pair
    expand: bool = False  # whether options should send by unpacking
    receiver: str | None = None  # the key to map to


SourceDict: TypeAlias = dict[str, str]


class Source(BaseModel):
    path: Path

    def __hash__(self) -> int:
        return hash(self.path)


class SourceHandler(BaseModel):
    provider: str
    options: Optional[Options] = Options()

    def __hash__(self) -> int:
        # this is singular per payload
        # so just hashing the provider
        return hash(self.provider)


class TaskPayload(BaseModel):
    provider: str
    options: Optional[Options] = Options()


class SourcePayload(BaseModel):
    sources: list[Source]
    source_handler: SourceHandler
    tasks: dict[str, TaskPayload]

    def __hash__(self) -> int:
        return hash(self.sources[0])


class TaskFunctionResult(BaseModel):
    source_uid: str
    result: Any
    kind: str
