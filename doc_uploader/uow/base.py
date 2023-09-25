from abc import ABC, abstractmethod

from doc_uploader.models.datamodels import BaseDBModel


class BaseUoW(ABC):
    def __init__(self, model: BaseDBModel) -> None:
        self.model = model
        super().__init__()

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
