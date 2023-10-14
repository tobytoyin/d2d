from doc_uploader.contracts.source import ObjectSource

from .mock.document import MockAdapter
from .obsidian.document import ObsidianAdapter


def create_document(source: ObjectSource):
    adapter = {
        "mock": MockAdapter,
        "obsidian": ObsidianAdapter,
    }.get(source.source_type)

    return adapter.create_document(source)
