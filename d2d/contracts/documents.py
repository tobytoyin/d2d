from pydantic import BaseModel, ConfigDict, field_validator


class DocumentComponent(BaseModel):
    """Type of components that compose a `Document`"""

    model_config = ConfigDict(frozen=True)

    @property
    def key(self) -> str:
        """The reference key in `Document` class"""
        raise NotImplementedError


class Summary(DocumentComponent):
    content: str = ""

    @property
    def key(self) -> str:
        return "summary"


class Document(BaseModel):
    uid: str
    summary: Summary = Summary()

    @field_validator("uid", mode="after")
    @classmethod
    def validate_uid_format(cls, v: str):
        # TODO no spaces, quotes, etc....
        return v
