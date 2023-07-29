import pytest

from obsidian_py_processor.processors import frontmatter_processor
from tests.test_markdowns import *


def test_frontmatter_processor_hv_meta(dummy_doc_with_frontmatter):
    expected = {'id': 'd-123123', 'name': 'my-dummy-doc'}
    result = frontmatter_processor(dummy_doc_with_frontmatter)
    assert result == expected


def test_frontmatter_processor_no_meta(dummy_doc_without_frontmatter):
    expected = {}
    result = frontmatter_processor(dummy_doc_without_frontmatter)
    assert result == expected
