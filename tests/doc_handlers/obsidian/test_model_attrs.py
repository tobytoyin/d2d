from doc_uploader.doc_processor.adapters.obsidian import *
from doc_uploader.doc_processor.interfaces import RelationProps
from tests.doc_handlers.obsidian.load_test_files import *


def test_document_id(doc_with_frontmatter):
    expected = "doc_with_frontmatter"  # filename without .ext
    result = doc_with_frontmatter.uid
    assert result == expected


def test_frontmatter_processor_hv_meta(doc_with_frontmatter):
    expected = {
        "doc_type": "test",
        "properties": {"name": "my-dummy-doc"},
    }
    result = doc_with_frontmatter.metadata.model_dump()
    assert result == expected


def test_frontmatter_processor_no_meta(doc_without_frontmatter):
    expected = {
        "doc_type": "unknown",
        "properties": {},
    }
    result = doc_without_frontmatter.metadata.model_dump()
    assert result == expected


def test_links_processor_hv_links(doc_with_links):
    expected = set(
        [
            RelationProps(
                rel_uid="document-id-1",
                rel_type="LINK",
                properties={"ref_text": ["alias 1"]},
            ),
            RelationProps(
                rel_uid="document-id-2",
                rel_type="LINK",
                properties={"ref_text": ["alias 2"]},
            ),
            RelationProps(
                rel_uid="document-id-3",
                rel_type="LINK",
                properties={"ref_text": []},
            ),
            RelationProps(
                rel_uid="document-id-4",
                rel_type="LINK",
                properties={"ref_text": ["ID"]},
            ),
        ]
    )
    result = doc_with_links.relations

    assert result == expected


def test_links_processor_no_links(doc_without_links):
    expected = set()
    result = doc_without_links.relations
    assert result == expected


def test_contents(doc_without_links):
    # TODO
    pass
