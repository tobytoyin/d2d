import os
from pathlib import Path

import pytest

from doc_uploader.contracts.document import Document
from doc_uploader.contracts.source import ObjectSource
from doc_uploader.processors import create_document


@pytest.fixture
def document_path():
    return Path("tests/test_docs/obsidian.md")


@pytest.fixture
def document(document_path):
    source_type = "obsidian"
    source = ObjectSource(path=document_path, source_type=source_type)
    return create_document(source)


def test_contents(document):
    document: Document = document
    assert document.content.contents == "hello world"


def test_source_path(document):
    document: Document = document
    assert str(document.source.path) == "tests/test_docs/obsidian.md"


def test_uid(document):
    document: Document = document
    assert str(document.uid) == "obsidian"
