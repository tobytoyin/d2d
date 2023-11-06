from pathlib import Path

from pydantic import BaseModel


class Source(BaseModel):
    path: Path
    options: dict[str, str] = {}
