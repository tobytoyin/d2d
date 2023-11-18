from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, field_validator


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    model_config = ConfigDict(frozen=True)

    @property
    def key(self) -> str:
        """The reference key in `Document` class"""
        raise NotImplementedError


class Summary(DocumentComponent):
    content: str = ""

    @property
    def key(self) -> str:
        return "summary"


class Metadata(DocumentComponent):
    doc_type: str = "document"

    @property
    def key(self) -> str:
        return "metadata"


class Relation(DocumentComponent):
    rel_uid: str
    rel_type: str
    properties: Optional[dict[str, Any]] = {}

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __hash__(self) -> int:
        return frozenset(self.model_dump()).__hash__()


class Relations(DocumentComponent):
    items: set[Relation] = set()

    @property
    def key(self) -> str:
        return "relations"


class Document(BaseModel):
    uid: str
    summary: Summary = Summary()
    metadata: Metadata = Metadata()
    relations: Relations = Relations()

    @field_validator("uid", mode="after")
    @classmethod
    def validate_uid_format(cls, v: str):
        # TODO no spaces, quotes, etc....
        return v
