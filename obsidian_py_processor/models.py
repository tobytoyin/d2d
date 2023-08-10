from abc import abstractmethod
from typing import Callable

from pydantic import BaseModel, ConfigDict

RelationsProcessorFn = Callable[[str], set]
MetadataProcessorFn = Callable[[str], dict]

class DocumentMetadata(BaseModel):
    """Class to convert dict int a Metadataclass"""
    model_config = ConfigDict(extra='allow')
    doc_type: str

class Document(BaseModel):
    relations_processor: RelationsProcessorFn = None
    metadata_processor : MetadataProcessorFn = None
    
    _contents: str = None  # str contents of the document
    _id: str = None
    
    path: str  # source path of the document
    
    @abstractmethod
    def read(self) -> str:
        ...
        
    @abstractmethod
    def id_resolver(self) -> str: 
        """Method to define how Document ID should be created"""
        ...
    
    @property   
    def contents(self) -> str:
        """Return the text contents of a Document"""
        if not self._contents:
            self._contents = self.read()
        
        return self._contents
    
    @property
    def id(self):
        if not self._id:
            self._id = self.id_resolver()
        
        return self._id
    
    @property
    def metadata(self):
        """Return the metadata of a Document"""
        metadata = self.metadata_processor(self.contents)
        return DocumentMetadata(**metadata)
    
    @property
    def links(self):
        """Return the Document ID of the links"""
        sets_of_links = self.relations_processor(self.contents)
        return 
        
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
    
    
    

    
    