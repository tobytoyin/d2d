from pydantic import BaseModel


class Source(BaseModel):
    path: str
    type: str
    options: dict
