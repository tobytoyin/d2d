import io

from d2d.contracts import document
from d2d.contracts.services import SourceTasks


# define the protocols and source types in this file here for registration
class MockSourceTasks_All(SourceTasks):
    source_io = lambda _: io.StringIO("text from dummy")
    links = lambda _: document.DocRelations()
    metadata = lambda _: document.DocMetadata()
    summary = lambda _: document.DocSummary()
    keywords = lambda _: document.DocKeywords()


class MockSourceTasks_Partial(SourceTasks):
    source_io = lambda _: io.StringIO("text from dummy")
