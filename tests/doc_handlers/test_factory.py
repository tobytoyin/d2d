from doc_uploader.doc_handlers.factory import (
    DocumentAdapterContainer,
    create_document,
    create_props,
    get_adapter,
)
from doc_uploader.doc_handlers.interfaces import Document, DocumentAdapter, DocumentProps

ALL_BUILDIN_ADAPTERS = set(["obsidian"])


@DocumentAdapterContainer.register(name="mock")
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

    def contents_normaliser(self):
        return "normalised hello world"


def test_factory_invoke_register():
    _ = get_adapter(name="mock", text="hello world")
    assert set([*DocumentAdapterContainer._map]) == set(["mock"]) | ALL_BUILDIN_ADAPTERS


def test_factory_creates_correct_class():
    adapter = get_adapter(name="mock", text="hello world")
    assert isinstance(adapter, DocumentAdapter)


def test_factory_create_props():
    props = create_props(adapter_name="mock", text="hello world")
    assert isinstance(props, DocumentProps)


def test_factory_create_document():
    props = create_document(adapter_name="mock", text="hello world")
    assert isinstance(props, Document)
