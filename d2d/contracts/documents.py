from pydantic import BaseModel


class DocumentComponent:
    """Type of components that compose a `Document`"""

    ...


class Summary(DocumentComponent, BaseModel):
    content: str = ""
