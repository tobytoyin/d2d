from typing import Callable, Protocol, Set, TextIO

from .document import DocumentMetadata, DocumentRelations
from .source import Source


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

    SourceIO: Callable[[Source], TextIO]  # use Source to return Reader Object

    # Services below preferrably should use SourceIO internally
    LinksTask: Callable[[Source], Set[DocumentRelations]]
    MetadataTask: Callable[[Source], DocumentMetadata]
