import doc_uploader.adapters.mock as mock
import doc_uploader.adapters.obsidian as obsidian
from doc_uploader.contracts.source import Source

from .mock.document import MockAdapter as MockDocument
from .obsidian.document import ObsidianAdapter as ObsidianDocument


def create_document(source: Source):
    adapter = {
        "mock": MockDocument,
        "obsidian": ObsidianDocument,
    }.get(source.source_type)

    return adapter.create_document(source)  # type: ignore


def get_adapter_service(source: Source, service_name: str):
    adapter = {
        "mock": mock.SourceHandlers,
        "obsidian": obsidian.SourceHandlers,
    }.get(source.source_type)

    service = {
        "source_reader": adapter.SOURCE_READER,
        "relations_extraction": adapter.LINK_PROCESSOR,
        "metadata_extraction": adapter.META_PROCESSOR,
    }.get(service_name)

    return service
