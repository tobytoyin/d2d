from typing import Any, Iterable, Optional

from pydantic import BaseModel, ConfigDict, field_validator


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    model_config = ConfigDict(frozen=True)

    @property
    def key(self) -> str:
        """The reference key in `Document` class"""
        raise NotImplementedError

    def prefix_model_dump(self, prefix=None):
        if not prefix:
            prefix = self.key + "_"

        d = self.model_dump()
        return {f"{prefix}{k}": v for k, v in d.items()}


class Content(DocumentComponent):
    """Contents of the Document

    text - text contents of the document
    location - optionally if text contents shouldn't be fully stored, a location reference
    codec - reference on how the text should be read, e.g., string, markdown, ...
    """

    text: str = ""
    location: str | None = None
    codec: str = "string"

    @property
    def key(self) -> str:
        return "content"


class Summary(DocumentComponent):
    content: str = ""

    @property
    def key(self) -> str:
        return "summary"


class Metadata(DocumentComponent):
    doc_type: str = "document"
    properties: dict[str, Any] = {}

    @property
    def key(self) -> str:
        return "metadata"


class Relation(DocumentComponent):
    rel_uid: str
    rel_type: str
    properties: dict[str, Any] = {}

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __hash__(self) -> int:
        return frozenset(self.model_dump()).__hash__()


class Relations(DocumentComponent):
    items: set[Relation] = set()

    @property
    def key(self) -> str:
        return "relations"


class Embedding(DocumentComponent):
    embedding: Iterable[float] = None

    @property
    def key(self) -> str:
        return "embedding"


class Document(BaseModel):
    uid: str
    content: Content = Content()
    summary: Summary = Summary()
    metadata: Metadata = Metadata()
    relations: Relations = Relations()
    embedding: Embedding = Embedding()

    @field_validator("uid", mode="after")
    @classmethod
    def validate_uid_format(cls, v: str):
        # TODO no spaces, quotes, etc....
        return v
