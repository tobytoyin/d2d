from doc_uploader.contracts.source import Source

from .mock.document import MockAdapter
from .obsidian.document import ObsidianAdapter


def create_document(source: Source):
    adapter = {
        "mock": MockAdapter,
        "obsidian": ObsidianAdapter,
    }.get(source.source_type)

    return adapter.create_document(source)  # type: ignore
