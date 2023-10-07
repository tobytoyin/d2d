from abc import ABC
from functools import cached_property
from typing import Any, Dict, Iterable, Set

from pydantic import BaseModel

from doc_uploader.doc_handlers.interfaces import DocRelations, Document

# Subclasses of BaseDBModel are used to formalised how different Document are translated
# into different types of databases models, e.g.,
# - Relational Database model
# - Graph Database model

# These databases models provides an standardised interface to reconstruct into queries/ uow
# based on different query languages


class DataModel(BaseModel):
    uid: str
    entity_type: str
    relations: Set[DocRelations]
    contents: str
    fields: Dict[str, Any]


class BaseDBModel(ABC):
    def __init__(self, document: Document) -> None:
        self.document = document

    @cached_property
    def dataobj(self) -> DataModel:
        document = self.document

        metadata = document.metadata.model_dump()
        doc_type = metadata.pop("doc_type")

        return DataModel(
            entity_type=doc_type,
            uid=document.uid,
            relations=document.relations,
            contents=document.contents,
            fields=metadata,
        )


class GraphModel(BaseDBModel):
    pass


class RDBModel(BaseDBModel):
    pass
