import pytest

from obsidian_py_processor.providers.obsidian.processors import *
from tests.load_test_files import *


def test_frontmatter_processor_hv_meta(doc_with_frontmatter):
    expected = {'id': 'd-123123', 'name': 'my-dummy-doc', 'doc_type': 'test'}
    result = doc_with_frontmatter.metadata.model_dump()
    assert result == expected


def test_frontmatter_processor_no_meta(doc_without_frontmatter):
    expected = {'doc_type': 'unknown'}
    result = doc_without_frontmatter.metadata.model_dump()
    assert result == expected


def test_links_processor_hv_links(doc_with_links):
    expected = set(['document-id-1', 'document-id-2', 'document-id-3'])
    result = links_processor(doc_with_links)
    assert result == expected


def test_links_processor_no_links(doc_without_links):
    expected = set()
    result = links_processor(doc_without_links)
    assert result == expected
