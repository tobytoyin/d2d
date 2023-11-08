from pathlib import Path
from typing import TypeAlias

from pydantic import BaseModel

SourcePayload: TypeAlias = dict[str, str]


class Source(BaseModel):
    path: Path
    options: dict[str, str] = {}
