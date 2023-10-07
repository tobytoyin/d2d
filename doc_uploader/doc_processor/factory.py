from typing import Type

from doc_uploader.common.factory import FactoryRegistry

from .interfaces import Document, DocumentAdapter, DocumentProps, MetadataProps, RelationProps


class DocumentAdapterContainer(FactoryRegistry[DocumentAdapter]):
    _map = {}
    import_pattern = "doc_processor/adapters/*/adapter.py"


def get_adapter(name: str, *args, **kwargs):
    adapters = DocumentAdapterContainer.get(name)
    if not adapters:
        raise ValueError

    return adapters(*args, **kwargs)


def create_props(adapter_name: str, *args, **kwargs):
    adapter = get_adapter(adapter_name, *args, **kwargs)
    return DocumentProps(adapter)


def create_document(adapter_name: str, *args, **kwargs):
    props = create_props(adapter_name, *args, **kwargs)

    # use the prop to return as a document
    return Document(
        uid=props.uid,
        contents=props.contents,
        metadata=props.metadata,
        relations=props.relations,
    )


def create_document_runtime(uid, doc_type, contents, relations, **fields):
    return Document(
        uid=uid,
        contents=contents,
        metadata=MetadataProps(doc_type=doc_type, properties=fields),
        relations=set([RelationProps(**rel) for rel in relations]),
    )
