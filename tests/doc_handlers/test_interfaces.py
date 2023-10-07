from pytest import fixture

from doc_uploader.doc_handlers.interfaces import (
    DocumentAdapter,
    DocumentProps,
    MetadataProps,
    RelationProps,
)
from doc_uploader.doc_handlers.types import NormalisedContents


# Assuming the adapter logics in parsing self.text are correct
# we test the interfaces is accessing the correct data provided
# by the adapter
class FakeDocumentAdapaterWithMeta(DocumentAdapter):
    def id_processor(self):
        return "doc-100"

    def metadata_processor(self):
        return {
            "doc_type": "test_document",
            "tags": ["a", "b", "c"],
        }

    def relations_processor(self):
        return [
            {"rel_uid": "doc-1", "rel_type": "LINK"},
            {"rel_uid": "doc-2", "rel_type": "LINK"},
        ]

    def contents_normaliser(self) -> NormalisedContents:
        return "normalised hello world"


class FakeDocumentAdapaterWithoutMeta(DocumentAdapter):
    def id_processor(self):
        return "doc-100"

    def metadata_processor(self):
        return {}

    def relations_processor(self):
        return [
            {
                "rel_uid": "doc-1",
                "rel_type": "LINK",
                "properties": {"extra_field": "1"},
            },
            {
                "rel_uid": "doc-2",
                "rel_type": "LINK",
                "properties": {"extra_field": "2"},
            },
        ]

    def contents_normaliser(self) -> NormalisedContents:
        return "normalised hello world"


@fixture
def mock_document_adapter_meta():
    return FakeDocumentAdapaterWithMeta()


@fixture
def mock_document_adapter_no_meta():
    return FakeDocumentAdapaterWithoutMeta()


### Below tests that the DocumentAdapter subclass can be interfaced with DocumentProps
### and generate the correct structure of the DocumentProps attributes


def test_prop_id(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    assert props.uid == "doc-100"


def test_prop_metadata(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)

    expected_meta = MetadataProps(
        doc_type="test_document",
        tags=["a", "b", "c"],
    )
    assert props.metadata == expected_meta


def test_prop_no_metadata(mock_document_adapter_no_meta):
    props = DocumentProps(mock_document_adapter_no_meta)

    expected_meta = MetadataProps()
    assert props.metadata == expected_meta


def test_prop_relations(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    expected_props = set(
        [
            RelationProps(rel_uid="doc-1", rel_type="LINK"),
            RelationProps(rel_uid="doc-2", rel_type="LINK"),
        ]
    )
    assert props.relations == expected_props


def test_prop_relations_wtih_extras(mock_document_adapter_no_meta):
    props = DocumentProps(mock_document_adapter_no_meta)

    expected_props = set(
        [
            RelationProps(rel_uid="doc-1", rel_type="LINK", properties={"extra_field": "1"}),
            RelationProps(rel_uid="doc-2", rel_type="LINK", properties={"extra_field": "2"}),
        ]
    )
    assert props.relations == expected_props


def test_prop_contents(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    assert props.contents == "normalised hello world"
