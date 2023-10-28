from abc import abstractmethod
from enum import Enum
from io import IOBase
from typing import (
    Callable,
    ClassVar,
    LiteralString,
    Optional,
    Protocol,
    Set,
    TextIO,
    TypeAlias,
)

from pydantic import BaseModel, ConfigDict

from .document import DocKeywords, DocMetadata, DocRelations, DocSummary
from .source import Source

IS_COMPATIBLE: TypeAlias = bool


class ServicesCatalog(Protocol):
    ...


class SourceTasks(ServicesCatalog):
    """Catalog of Service Functions that accept `Source` Type as Input

    - `SourceIO` - use `Source` to return an Reader for text

    Below are the Services that are preferrably take `Source` as functional\
    input but internally call `SourceIO` to reduce overheads:
    
    - `LinksTask` - task that extracts set of relationships to other Documents
    - `MetadataTask` - task that extracts metadata within a Document
    """

    compatible_source: Optional[Set[LiteralString]] = set()

    # use Source to return Reader Object
    source_io: Callable[[Source], IOBase]

    # Services below preferrably should use SourceIO internally
    links: Callable[[Source], DocRelations]
    metadata: Callable[[Source], DocMetadata]
    summary: Callable[[Source], DocSummary]
    keywords: Callable[[Source], DocKeywords]

    @classmethod
    def _validate_source_io_exists(cls) -> None:
        if not cls.source_io:
            raise NotImplementedError

    @classmethod
    def _check_compatible(cls, source: Source) -> IS_COMPATIBLE:
        """Helper method to check if the Adapter supports specific Source type

        :param source: the source object requires to call on the Tasks
        :type source: Source
        """

        if not cls.compatible_source:
            return True

        if source.source_type in cls.compatible_source:
            return True

        return False
