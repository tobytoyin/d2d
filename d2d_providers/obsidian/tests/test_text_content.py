from .. import TaskCatalog
from ..processor import image_ref_to_url
from .fixtures import doc1


def test_contents_without_frontmatter():
    contents = """
    Hello world!
    """

    expected = {
        "text": "Hello world!",
        "codec": "markdown",
    }

    assert expected == TaskCatalog.content(contents)


def test_contents_with_frontmatter():
    contents = """
    ---
    type: file
    ---
    Hello world!
    """

    expected_content = """
    Hello world!
    """.strip()

    expected = {
        "text": expected_content,
        "codec": "markdown",
    }

    import re

    d = re.sub(r"^---\s+.+?\s+---", "", contents).strip()
    print(d)

    assert expected == TaskCatalog.content(contents)


def test_contents_with_frontmatter_and_sepline():
    contents = """
    ---
    type: file
    ---
    Hello world!

    ---
    section 2 after line break

    """

    expected_content = """
    Hello world!

    ---
    section 2 after line break

    """.strip()

    expected = {
        "text": expected_content,
        "codec": "markdown",
    }

    assert expected == TaskCatalog.content(contents)


def test_modifying_image_to_url(doc1):
    res = image_ref_to_url(doc1, "http://")

    print(res)
