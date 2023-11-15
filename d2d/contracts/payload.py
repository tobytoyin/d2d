from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Literal, Optional, TypeAlias

from pydantic import BaseModel, ValidationError, field_validator


class Options(BaseModel):
    mapping: dict[str, Any] | None = None  # the kwarg-value pair
    expand: bool = False  # whether options should send by unpacking
    receiver: str | None = None  # the key to map to


SourceDict: TypeAlias = dict[str, str]
TaskKeyword: TypeAlias = Literal["summary"]


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


class TaskSpec(BaseModel):
    provider: str
    options: Optional[Options] = Options()


class SourcePayload(BaseModel):
    sources: list[Source]
    source_handler: SourceHandler
    tasks: dict[TaskKeyword, TaskSpec]

    def __hash__(self) -> int:
        return hash(self.sources[0])

    @field_validator("sources", mode="before")
    @classmethod
    def filter_invalid_sources(cls, v: str):
        for i, s in enumerate(v):
            try:
                yield Source.model_validate(s)

            except ValidationError:
                logging.warning("sources[%d] is not compatible and removed.", i)
                continue


class TaskFunctionResult(BaseModel):
    source_uid: str
    result: Any
    kind: str
