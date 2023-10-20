from pathlib import Path
from typing import TextIO

from pydantic import BaseModel, ConfigDict

# Source is the first Contact Point of an object going through the pipeline


class Source(BaseModel):
    """_summary_

    :param BaseModel: _description_
    :type BaseModel: _type_
    """

    path: Path
    source_type: str

    model_config = ConfigDict(extra="allow")
    # attribute can be expanded dynamically based on each adapter own usages

    def __hash__(self) -> int:
        return hash(self.path)
