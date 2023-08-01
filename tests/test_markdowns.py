import pytest
import yaml


@pytest.fixture
def doc_with_frontmatter() -> str:
    with open('./tests/test_docs/doc_with_frontmatter.md', 'r') as f:
        text = f.read()
        return text

@pytest.fixture
def doc_without_frontmatter() -> str:
    with open('./tests/test_docs/doc_without_frontmatter.md', 'r') as f:
        text = f.read()
        return text

        
@pytest.fixture
def doc_with_links() -> str:
    with open('./tests/test_docs/doc_with_internal_links.md', 'r') as f:
        text = f.read()
        return text


@pytest.fixture
def doc_without_links() -> str:
    with open('./tests/test_docs/doc_without_internal_links.md', 'r') as f:
        text = f.read()
        return text