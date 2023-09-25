from abc import ABC
from typing import Any, Dict, Set

from pydantic import BaseModel

from doc_uploader.doc_handlers.base import BaseDocument

# Subclasses of BaseDBModel are used to formalised how different BaseDocument are translated
# into different types of databases models, e.g.,
# - Relational Database model
# - Graph Database model

# These databases models provides an standardised interface to reconstruct into queries/ uow
# based on different query languages


class DataModel(BaseModel):
    id: str
    entity_type: str
    relations: Set[str]
    fields: Dict[str, Any]


class BaseDBModel(ABC):
    def __init__(self, document: BaseDocument) -> None:
        self.document = document

    @property
    def base_properties(self) -> DataModel:
        document = self.document

        return DataModel(
            entity_type=document.entity_type,
            id=document.id,
            relations=document.relations,
            fields=document.metadata,
        )

    def dict(self) -> dict:
        return self.base_properties.model_dump()

    def json(self) -> str:
        return self.base_properties.model_dump_json()


class GraphModel(BaseDBModel):
    pass


class RDBModel(BaseDBModel):
    pass
