from abc import abstractmethod
from typing import Protocol

from doc_uploader.contracts.document import Document


class DocumentToDB(Protocol):
    document: Document

    @abstractmethod
    def update_or_create_document(self, *args, **kwargs) -> bool:
        """Method to create a single document entity in the database"""
        ...

    @abstractmethod
    def update_or_create_relationships(self, *args, **kwargs) -> bool:
        """Method to create one-to-many relationships

        Create one document --> many relationships to documents

        """
        ...

    @abstractmethod
    def delete_document(self, *args, **kwargs) -> bool:
        ...
