from pathlib import Path

import pytest

from doc_uploader.adapters.factory import create_document
from doc_uploader.contracts.document import Document, DocumentRelations
from doc_uploader.contracts.source import Source


@pytest.fixture
def document_path():
    return Path("tests/test_docs/obsidian.md")


@pytest.fixture
def document(document_path):
    source_type = "obsidian"
    source = Source(path=document_path, source_type=source_type)
    return create_document(source)


@pytest.fixture
def doc_with_frontmatter():
    source_type = "obsidian"
    path = Path("tests/test_docs/doc_with_frontmatter.md")
    source = Source(path=path, source_type=source_type)
    return create_document(source)


@pytest.fixture
def doc_without_frontmatter():
    source_type = "obsidian"
    path = Path("tests/test_docs/doc_without_frontmatter.md")
    source = Source(path=path, source_type=source_type)
    return create_document(source)


@pytest.fixture
def doc_with_links():
    source_type = "obsidian"
    path = Path("tests/test_docs/doc_with_internal_links.md")
    source = Source(path=path, source_type=source_type)
    return create_document(source)


@pytest.fixture
def doc_without_links():
    source_type = "obsidian"
    path = Path("tests/test_docs/doc_without_internal_links.md")
    source = Source(path=path, source_type=source_type)
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


def test_frontmatter_processor_hv_metadata(doc_with_frontmatter):
    expected = {
        "doc_type": "test",
        "properties": {"name": "my-dummy-doc"},
    }
    result = doc_with_frontmatter.metadata.model_dump()
    assert result == expected


def test_frontmatter_processor_no_meta(doc_without_frontmatter):
    expected = {
        "doc_type": "unknown",
        "properties": {},
    }
    result = doc_without_frontmatter.metadata.model_dump()
    assert result == expected


def test_links_processor_hv_links(doc_with_links):
    expected = set(
        [
            DocumentRelations(
                rel_uid="document-id-1",
                rel_type="LINK",
                properties={"ref_text": ["alias 1"]},
            ),
            DocumentRelations(
                rel_uid="document-id-2",
                rel_type="LINK",
                properties={"ref_text": ["alias 2"]},
            ),
            DocumentRelations(
                rel_uid="document-id-3",
                rel_type="LINK",
                properties={"ref_text": []},
            ),
            DocumentRelations(
                rel_uid="document-id-4",
                rel_type="LINK",
                properties={"ref_text": ["ID"]},
            ),
        ]
    )
    result = doc_with_links.relations

    assert result == expected


def test_links_processor_no_links(doc_without_links):
    expected = set()
    result = doc_without_links.relations
    assert result == expected
