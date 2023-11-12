from pydantic import BaseModel, ConfigDict


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    model_config = ConfigDict(frozen=True)

    @property
    def key(self):
        """The reference key in `Document` class"""
        raise NotImplementedError


class Summary(DocumentComponent):
    content: str = ""

    @property
    def key(self):
        return "summary"


class Document(BaseModel):
    uid: str
    summary: Summary
