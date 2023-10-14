from pathlib import Path

from doc_uploader.contracts.source import ObjectSource
from doc_uploader.processors import create_document


def test_create_document():
    doc = create_document(ObjectSource(path=Path("."), source_type="mock"))

    assert doc.source.source_type == "mock"
