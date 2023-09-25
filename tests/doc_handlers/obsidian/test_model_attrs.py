from doc_uploader.doc_handlers.obsidian import *
from tests.doc_handlers.obsidian.load_test_files import *


def test_document_id(doc_with_frontmatter):
    expected = "doc_with_frontmatter"  # filename without .ext
    result = doc_with_frontmatter.id
    assert result == expected


def test_frontmatter_processor_hv_meta(doc_with_frontmatter):
    expected = {"name": "my-dummy-doc"}
    result = doc_with_frontmatter.metadata
    assert result == expected


def test_frontmatter_processor_no_meta(doc_without_frontmatter):
    expected = {}
    result = doc_without_frontmatter.metadata
    assert result == expected


def test_entity_type_hv_doc_type(doc_with_frontmatter):
    expected = "test"
    result = doc_with_frontmatter.entity_type
    assert result == expected


def test_entity_type_hv_no_doc_type(doc_without_frontmatter):
    expected = "unknown"
    result = doc_without_frontmatter.entity_type
    assert result == expected


def test_links_processor_hv_links(doc_with_links):
    expected = set(["document-id-1", "document-id-2", "document-id-3"])
    result = doc_with_links.relations
    assert result == expected


def test_links_processor_no_links(doc_without_links):
    expected = set()
    result = doc_without_links.relations
    assert result == expected


def test_contents(doc_without_links):
    # TODO
    pass
