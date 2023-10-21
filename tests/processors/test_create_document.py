from pathlib import Path

from d2d.adapters.factory import create_document
from d2d.contracts.source import Source


def test_create_document():
    doc = create_document(Source(path=Path("."), source_type="mock"))

    assert doc.source.source_type == "mock"
