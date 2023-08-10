from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Document(ABC):
    path: str
    _contents: str = None
    
    # def process_metadata(self, processor_func: Callable[[str], dict]):
    #     ...
    
    @abstractmethod
    def read(self) -> str:
        ...
    
    @property   
    def contents(self):
        """Return the text contents of a Document"""
        if not self._contents:
            self._contents = self.read()
        
        return self._contents

        
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
    
    
    

    
    