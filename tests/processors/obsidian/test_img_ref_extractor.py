# import os
# from pathlib import Path

# import pytest

# from doc_uploader.contracts.source import DocumentSource
# from doc_uploader.processors.obsidian.document import Contents
# from doc_uploader.processors.obsidian.image_ref_extractor import ObsidianRefExtractor


# @pytest.fixture
# def document_path():
#     return Path("tests/test_docs/images_links.md")


# @pytest.fixture
# def content(document_path):
#     source = DocumentSource(path=document_path, source_type="md")
#     return Contents(source=source)


# def test_reference_extractor(content):
#     extractor = ObsidianRefExtractor(root=Path("myroot"))
#     image_sources = extractor.image_sources(content)

#     # get the path only
#     paths = set([str(source.path) for source in image_sources])
#     print(paths)

#     assert paths == set(
#         [
#             "myroot/image-name-1.png",
#             "myroot/image-name-2.jpg",
#             "myroot/image-name-3.png",
#         ]
#     )
