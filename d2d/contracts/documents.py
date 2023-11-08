from pydantic import BaseModel


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""


class Summary(DocumentComponent):
    content: str = ""
