from doc_uploader.doc_handlers.factory import Registry, get_adapter, register_all
from doc_uploader.doc_handlers.interfaces import DocumentAdapter


def test_register_has_adapter():
    register_all()
    print(Registry.registry)

    assert "obsidian" in Registry.registry


def test_factory_creates_correct_class():
    adapter = get_adapter(name="obsidian", text="hello world", path="dummy_path")
    assert isinstance(adapter, DocumentAdapter)
