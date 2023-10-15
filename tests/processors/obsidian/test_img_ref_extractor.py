import os
from pathlib import Path

import pytest

from doc_uploader.adapters.factory import create_document
from doc_uploader.adapters.obsidian.extract_image_sources import ObsidianRefExtractor
from doc_uploader.contracts.source import Source


@pytest.fixture
def document_path():
    return Path("tests/test_docs/images_links.md")


@pytest.fixture
def document(document_path):
    source_type = "obsidian"
    source = Source(path=document_path, source_type=source_type)
    return create_document(source)


def test_reference_extractor(document):
    extractor = ObsidianRefExtractor(document=document, root=Path("myroot"))
    image_sources = extractor.image_sources()

    # get the path only
    paths = set([str(source.path) for source in image_sources])

    assert paths == set(
        [
            "myroot/image-name-1.png",
            "myroot/image-name-2.jpg",
            "myroot/image-name-3.png",
        ]
    )


def test_label_extracted(document):
    extractor = ObsidianRefExtractor(document=document, root=Path("myroot"))
    image_sources = extractor.image_sources()

    # get the path only
    labels = [str(source.label) for source in image_sources]

    assert len(labels) == 3
    assert set(labels) == set(["id-1", ""])
