from pytest import fixture

from doc_uploader.doc_handlers.interfaces import DocMetadata, DocumentAdapter, DocumentProps
from doc_uploader.doc_handlers.types import NormalisedContents

# Assuming the adapter logics in parsing self.text are correct
# we test the interfaces is accessing the correct data provided
# by the adapter


class FakeDocumentAdapaterWithMeta(DocumentAdapter):
    def __init__(self, text="hello world") -> None:
        super().__init__(text)

    def id_processor(self):
        return "doc-100"

    def metadata_processor(self):
        return {
            "doc_type": "test_document",
            "tags": ["a", "b", "c"],
        }

    def relations_processor(self):
        return set(["doc-1", "doc-2"])

    def contents_normaliser(self) -> NormalisedContents:
        return "normalised hello world"


class FakeDocumentAdapaterWithoutMeta(DocumentAdapter):
    def __init__(self, text="hello world") -> None:
        super().__init__(text)

    def id_processor(self):
        return "doc-100"

    def metadata_processor(self):
        return {}

    def relations_processor(self):
        return set(["doc-1", "doc-2"])

    def contents_normaliser(self) -> NormalisedContents:
        return "normalised hello world"


@fixture
def mock_document_adapter_meta():
    return FakeDocumentAdapaterWithMeta()


@fixture
def mock_document_adapter_no_meta():
    return FakeDocumentAdapaterWithoutMeta()


def test_prop_id(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    assert props.id == "doc-100"


def test_prop_metadata(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)

    expected_meta = DocMetadata(doc_type="test_document", tags=["a", "b", "c"])
    assert props.metadata == expected_meta


def test_prop_no_metadata(mock_document_adapter_no_meta):
    props = DocumentProps(mock_document_adapter_no_meta)

    expected_meta = DocMetadata()
    assert props.metadata == expected_meta


def test_prop_relations(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    assert props.relations == set(["doc-1", "doc-2"])


def test_prop_contents(mock_document_adapter_meta):
    props = DocumentProps(mock_document_adapter_meta)
    assert props.contents == "normalised hello world"
