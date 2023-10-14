from functools import cached_property
from pathlib import Path

import pytest

from doc_uploader.contracts._source import DocumentSource
from doc_uploader.processors.document.adapters.obsidian import ObsidianMd


@pytest.fixture
def document_path():
    return Path("tests/test_docs/obsidian.md")


@pytest.fixture
def md_object(document_path):
    return ObsidianMd(source=document_path, file_type="md")


def test_contents(md_object):
    md_object: ObsidianMd = md_object
    assert md_object.contents == "hello world"
