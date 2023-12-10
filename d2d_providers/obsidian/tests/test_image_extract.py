import pytest

from ..processor import image_extraction


@pytest.fixture
def doc1():
    with open("d2d_providers/obsidian/tests/documents/image_file.md", "r") as f:
        return f.read()


def test_image_extraction_with_render_regex(doc1):
    results = image_extraction(doc1)
    assert set(results) == set(
        [
            "some-path/some-img1.png",
            "some-path/some-img2.jpg",
            "some-path/some-img3.jpg",
            "some-path/some-img4.jpg",
        ]
    )
