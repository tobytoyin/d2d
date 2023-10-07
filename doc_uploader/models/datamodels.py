from abc import ABC
from functools import cached_property
from typing import Any, Dict, Iterable, Sequence, Set

from pydantic import BaseModel, ConfigDict

from doc_uploader.doc_handlers.interfaces import Document, RelationProps

# Subclasses of BaseDBModel are used to formalised how different Document are translated
# into different types of databases models, e.g.,
# - Relational Database model
# - Graph Database model


# These databases models provides an standardised interface to reconstruct into queries/ uow
# based on different query languages
class GraphDataModel(BaseModel):
    uid: str
    node_type: str
    contents: str
    relations: Sequence[RelationProps]
    fields: Dict[str, Any]


class Row(BaseModel):
    class _RelationsFields(BaseModel):
        model_config = ConfigDict(extra="allow")

    class _MetadataFields(BaseModel):
        model_config = ConfigDict(extra="allow")

    uid: str
    rel_uid: str


class TabularDataModel(BaseModel):
    rows: Iterable[Row]
