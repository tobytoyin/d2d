from abc import ABC, abstractmethod
from typing import Callable, List

from pydantic import BaseModel, ConfigDict


class DocumentMetadata(BaseModel):
    """Class to convert dict int a Metadataclass"""
    model_config = ConfigDict(extra='allow')
    doc_type: str

class Document(BaseModel):
    links_processor: Callable[[str], set] = None
    metadata_processor: Callable[[str], dict] = None
    _contents: str = None
    path: str
    
        
    # def __init__(self, path: str) -> None:
    #     super().__init__()
    #     self.path = path
    #     self._contents: str = None
    
    @abstractmethod
    def read(self) -> str:
        ...
    
    @property   
    def contents(self):
        """Return the text contents of a Document"""
        if not self._contents:
            self._contents = self.read()
        
        return self._contents
    
    @property
    def metadata(self):
        """Return the metadata of a Document"""
        metadata = self.metadata_processor(self.contents)
        return DocumentMetadata(**metadata)
        
    # @abstractmethod
    # def create_datamodel(self):
    #     ...
        
    
#     text: str
#     tags: List[str]
#     terms: List[str]
    
    
# @dataclass
# class GraphDocumentModel(Document):

    
#     def return_document(self):
#         return {
#             'text': self.text,
#             'tags': self.tags, 
#         }
    
    
    

    
    