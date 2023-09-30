import pytest

from doc_uploader.doc_handlers.interfaces import DocumentProps
from doc_uploader.doc_handlers.obsidian.adapter import ObsidianAdapter

TEST_DOC_PREFIX = "./tests/doc_handlers/obsidian"


@pytest.fixture
def doc_with_frontmatter() -> ObsidianAdapter:
    path = f"{TEST_DOC_PREFIX}/test_docs/doc_with_frontmatter.md"

    with open(path, "r") as f:
        text = f.read()
    return DocumentProps(ObsidianAdapter(text=text, path=path))


@pytest.fixture
def doc_without_frontmatter():
    path = f"{TEST_DOC_PREFIX}/test_docs/doc_without_frontmatter.md"

    with open(path, "r") as f:
        text = f.read()
    return DocumentProps(ObsidianAdapter(text=text, path=path))


@pytest.fixture
def doc_with_links():
    path = f"{TEST_DOC_PREFIX}/test_docs/doc_with_internal_links.md"

    with open(path, "r") as f:
        text = f.read()
    return DocumentProps(ObsidianAdapter(text=text, path=path))


@pytest.fixture
def doc_without_links():
    path = f"{TEST_DOC_PREFIX}/test_docs/doc_without_internal_links.md"

    with open(path, "r") as f:
        text = f.read()
    return DocumentProps(ObsidianAdapter(text=text, path=path))
