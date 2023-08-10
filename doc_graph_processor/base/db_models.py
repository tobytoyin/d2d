from abc import ABC

from base.doc_models import BaseDocument
from pydantic import BaseModel


class BaseDBModel(ABC, BaseModel):
    document: BaseDocument

    @property
    def base_properties(self) -> dict:
        document = self.document

        return {
            'id': document.id,
            'relations': document.relations,
            **document.metadata.model_dump(),
        }

    @property
    def record(self) -> dict:
        return self.base_properties


class GraphDocumentModel(BaseDBModel):
    ...
