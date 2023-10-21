from abc import abstractmethod
from typing import Callable, LiteralString, Optional, Protocol, Set, TextIO, TypeAlias

from .document import (
    DocumentKeywords,
    DocumentMetadata,
    DocumentRelation,
    DocumentSummary,
)
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

    _compatible_source: Optional[Set[LiteralString]] = None

    # use Source to return Reader Object
    SourceIO: Callable[[Source], TextIO]

    # Services below preferrably should use SourceIO internally
    LinksTask: Callable[[Source], Set[DocumentRelation]]
    MetadataTask: Callable[[Source], DocumentMetadata]
    SummaryTask: Callable[[Source], DocumentSummary]
    KeywordsTask: Callable[[Source], DocumentKeywords]

    @classmethod
    def _check_compatible(cls, source: Source) -> IS_COMPATIBLE:
        """Helper method to check if the Adapter supports specific Source type

        :param source: the source object requires to call on the Tasks
        :type source: Source
        """

        if not cls._compatible_source:
            return True

        if source.source_type in cls._compatible_source:
            return True

        return False
