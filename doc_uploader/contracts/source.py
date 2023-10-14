from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel, ConfigDict

# Source is the first Contact Point of an object going through the pipeline


class ImageSource(BaseModel):
    """Input model for an Image source

    Image source can be local, cloud-base, internet
    """

    path: Path
    source_type: str

    def __hash__(self) -> int:
        return hash(self.path)


class ObjectSource(BaseModel):
    """_summary_

    :param BaseModel: _description_
    :type BaseModel: _type_
    """

    path: Path
    source_type: str
    model_config = ConfigDict(extra="allow")  # for adapter specific keywords

    def __hash__(self) -> int:
        return hash(self.path)
