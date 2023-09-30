from typing import Type

from doc_uploader.common.factory import FactoryRegistry

from .interfaces import DocMetadata, Document, DocumentAdapter, DocumentProps


class DocumentAdapterContainer(FactoryRegistry[DocumentAdapter]):
    _map = {}
    import_pattern = "doc_handlers/adapters/*/adapter.py"


def get_adapter(name: str, *args, **kwargs):
    adapters = DocumentAdapterContainer.get(name)
    print(DocumentAdapterContainer._map)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)


def create_props(adapter_name: str, *args, **kwargs):
    adapter = get_adapter(name=adapter_name, *args, **kwargs)
    return DocumentProps(adapter)


def create_document(adapter_name: str, *args, **kwargs):
    props = create_props(adapter_name=adapter_name, *args, **kwargs)

    # use the prop to return as a document
    return Document(
        uid=props.id,
        contents=props.contents,
        metadata=props.metadata,
        relations=props.relations,
    )


def create_document_runtime(uid, doc_type, contents, relations, **fields):
    return Document(
        uid=uid,
        doc_type=doc_type,
        contents=contents,
        metadata=DocMetadata(doc_type=doc_type, **fields),
        relations=relations,
    )
