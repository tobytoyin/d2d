from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Literal, Optional, TypeAlias

from pydantic import BaseModel, Field, ValidationError, field_validator

from d2d.contracts.enums import TaskKeyword

SourceDict: TypeAlias = dict[str, str]


class Options(BaseModel):
    mapping: dict[str, Any] | None = None  # the kwarg-value pair
    expand: bool = False  # whether options should send by unpacking
    receiver: str | None = None  # the key to map to


class Source(BaseModel):
    path: Path

    def __hash__(self) -> int:
        return hash(self.path)


class SourceSpec(BaseModel):
    provider: str
    options: Optional[Options] = Options()

    def __hash__(self) -> int:
        # this is singular per payload
        # so just hashing the provider
        return hash(self.provider)


class TaskSpec(BaseModel):
    provider: str
    options: Optional[Options] = Options()


class DocumentService(BaseModel):
    plugin_name: str
    service_name: str


class JobPayload(BaseModel):
    sources: list[Source]
    source_spec: SourceSpec
    tasks: dict[TaskKeyword, TaskSpec]
    document_services: list[DocumentService] | None = Field(default_factory=list)

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
    kind: str
    result: Any
