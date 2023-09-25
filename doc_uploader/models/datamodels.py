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
    def dataobj(self) -> DataModel:
        document = self.document

        return DataModel(
            entity_type=document.entity_type,
            id=document.id,
            relations=document.relations,
            fields=document.metadata,
        )

    @property
    def dict(self) -> dict:
        obj = self.dataobj.model_dump()
        fields = obj.pop("fields")
        obj.update(fields)
        return obj

    # @property
    # def json(self) -> str:
    #     return self.dataobj.model_dump_json()


class GraphModel(BaseDBModel):
    pass


class RDBModel(BaseDBModel):
    pass
