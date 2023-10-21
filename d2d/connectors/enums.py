from enum import Enum
from typing import Literal, Protocol, TypeAlias

from pydantic import BaseModel

from d2d.protocols._document_to_db import DocumentToDB


class Endpoints(str, Enum):
    NEO4J = "neo4j"
    MOCK = "mock"


class Services(Protocol):
    document_to_database: DocumentToDB | None = None
