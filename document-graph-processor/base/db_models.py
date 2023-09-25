from abc import ABC, abstractmethod

from base.doc_models import BaseDocument
from pydantic import BaseModel

# Subclasses of BaseDBModel are used to formalised how different BaseDocument are translated
# into different types of databases models, e.g., 
# - Relational Database model
# - Graph Database model

# These databases models provides an standardised interface to reconstruct into queries/ uow 
# based on different query languages

class BaseDBModel(ABC, BaseModel):
    document: BaseDocument

    @property
    def base_properties(self) -> dict:
        document = self.document
        metadata = document.metadata.model_dump()
        return {
            'node_type': metadata.pop('doc_type'),
            'id': document.id,
            'relations': document.relations,
            'fields': {**metadata},
        }

    @property
    def record(self) -> dict:
        return self.base_properties

class GraphDocumentModel(BaseDBModel):
    ...
    
class RelationalDocumentModel(BaseDBModel):
    ...
        
