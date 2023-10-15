from pathlib import Path

from doc_uploader.adapters.factory import create_document
from doc_uploader.contracts.source import Source


def test_create_document():
    doc = create_document(Source(path=Path("."), source_type="mock"))

    assert doc.source.source_type == "mock"
