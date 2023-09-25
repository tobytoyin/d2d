from abc import ABC, abstractmethod


class BaseUoW(ABC):
    @abstractmethod
    def _valid_datamodels(self):
        ...

    @abstractmethod
    def update_or_create_document(self, *args, **kwargs):
        """Method to create a single document entity in the database"""
        ...

    @abstractmethod
    def update_or_create_relationships(self, *args, **kwargs):
        """Method to create one-to-many relationships

        Create one document --> many relationships to documents

        """
        ...
