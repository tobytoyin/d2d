import json
from typing import Any, Iterable, Optional
import re

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
    source: str | None = None
    vector: list[float] | None = None
    model: str | None = None
    dimension: int = 0

    @property
    def key(self) -> str:
        return "embedding"


class ObjectReferences(DocumentComponent):
    # container to store list of paths that reference objects from
    # some path/ url locations
    paths: Optional[Iterable[str]] = None
    prefix: str = ""

    @property
    def key(self) -> str:
        return "obj_refs"

    @property
    def object_names(self):
        if self.paths is None:
            return
        return map(lambda e: e.split("/")[-1], self.paths)


class NamedEntity(BaseModel):
    id: str
    type: str
    properties: dict[str, str] = {}

    @field_validator("type")
    def type_camelcase(cls, v: str):
        return ''.join(v.split(' '))

    @field_validator("id")
    def id_lower(cls, v: str):
        v = v.lower()
        return '_'.join(v.split(' '))


class EntitiesRelation(BaseModel):
    root: str
    type: str
    target: str
    properties: dict[str, str] = {}

    @field_validator("root")
    def root_lower(cls, v: str):
        v = v.lower()
        return '_'.join(v.split(' '))

    @field_validator("target")
    def target_lower(cls, v: str):
        v = v.lower()
        return '_'.join(v.split(' '))  

    @field_validator("type")
    def type_no_specialchar(cls, v: str):
        v = re.sub('[^a-zA-Z0-9 \n\.]', '_', v)
        v = '_'.join(v.split(' '))
        return v.upper()


class NamedEntitiesRelations(DocumentComponent):
    source: str | None = None
    model: str | None = None
    entities: list[NamedEntity] = None
    relations: list[EntitiesRelation] = None

    @property
    def key(self) -> str:
        return "ner"


class Document(BaseModel):
    uid: str
    content: Content = Content()
    summary: Summary = Summary()
    metadata: Metadata = Metadata()
    relations: Relations = Relations()
    embedding: Embedding = Embedding()
    obj_refs: ObjectReferences = ObjectReferences()
    ner: NamedEntitiesRelations = NamedEntitiesRelations()

    @field_validator("uid", mode="after")
    @classmethod
    def validate_uid_format(cls, v: str):
        # TODO no spaces, quotes, etc....
        return v
