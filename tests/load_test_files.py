import pytest
import yaml

from obsidian_py_processor.providers.obsidian.models import ObsidianDocument


@pytest.fixture
def doc_with_frontmatter() -> str:
    return ObsidianDocument(path='./tests/test_docs/doc_with_frontmatter.md')


@pytest.fixture
def doc_without_frontmatter() -> str:
    return ObsidianDocument(path='./tests/test_docs/doc_without_frontmatter.md')


@pytest.fixture
def doc_with_links() -> str:
    return ObsidianDocument(path='./tests/test_docs/doc_with_internal_links.md')


@pytest.fixture
def doc_without_links() -> str:
    return ObsidianDocument(path='./tests/test_docs/doc_without_internal_links.md')
