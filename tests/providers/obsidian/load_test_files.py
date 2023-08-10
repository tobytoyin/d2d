import pytest
import yaml

from doc_graph_processor.providers.obsidian.models import ObsidianDocument

TEST_DOC_PREFIX = './tests/providers/obsidian'


@pytest.fixture
def doc_with_frontmatter() -> ObsidianDocument:
    return ObsidianDocument(path=f'{TEST_DOC_PREFIX}/test_docs/doc_with_frontmatter.md')


@pytest.fixture
def doc_without_frontmatter() -> ObsidianDocument:
    return ObsidianDocument(path=f'{TEST_DOC_PREFIX}/test_docs/doc_without_frontmatter.md')


@pytest.fixture
def doc_with_links() -> ObsidianDocument:
    return ObsidianDocument(path=f'{TEST_DOC_PREFIX}/test_docs/doc_with_internal_links.md')


@pytest.fixture
def doc_without_links() -> ObsidianDocument:
    return ObsidianDocument(path=f'{TEST_DOC_PREFIX}/test_docs/doc_without_internal_links.md')
