import pytest
import yaml


@pytest.fixture
def dummy_doc_with_frontmatter() -> str:
    with open('./tests/test_docs/doc_with_frontmatter.md', 'r') as f:
        
        text = f.read()
        return text

@pytest.fixture
def dummy_doc_without_frontmatter() -> str:
    with open('./tests/test_docs/doc_without_frontmatter.md', 'r') as f:
        
        text = f.read()
        return text