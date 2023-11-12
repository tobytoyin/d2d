from pydantic import BaseModel


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    @property
    def key(self):
        """The reference key in `Document` class"""
        ...


class Summary(DocumentComponent):
    content: str = ""

    @property
    def key(self):
        return "summary"


class Document(BaseModel):
    uid: str
    summary: Summary
