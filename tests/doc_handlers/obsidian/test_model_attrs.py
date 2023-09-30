from doc_uploader.doc_handlers.adapters.obsidian import *
from tests.doc_handlers.obsidian.load_test_files import *


def test_document_id(doc_with_frontmatter):
    expected = "doc_with_frontmatter"  # filename without .ext
    result = doc_with_frontmatter.uid
    assert result == expected


def test_frontmatter_processor_hv_meta(doc_with_frontmatter):
    expected = {"doc_type": "test", "name": "my-dummy-doc"}
    result = doc_with_frontmatter.metadata.model_dump()
    assert result == expected


def test_frontmatter_processor_no_meta(doc_without_frontmatter):
    expected = {"doc_type": "unknown"}
    result = doc_without_frontmatter.metadata.model_dump()
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
