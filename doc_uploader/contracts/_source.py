from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel


class ImageSource(ABC, BaseModel):
    """Input model for an Image source

    Image source can be local, cloud-base, internet
    """

    source: Path
    file_type: str

    @property
    @abstractmethod
    def bytes(self) -> bytes:
        ...


class DocumentSource(ABC, BaseModel):
    """_summary_

    :param BaseModel: _description_
    :type BaseModel: _type_
    """

    source: Path
    file_type: str

    @property
    @abstractmethod
    def contents(self) -> str:
        # method to read the source and return string contents
        ...

    @property
    @abstractmethod
    def bytes(self) -> bytes:
        # method to read the source and return bytes contents
        ...
