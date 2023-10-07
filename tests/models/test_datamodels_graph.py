from pprint import PrettyPrinter

from doc_uploader.doc_handlers.factory import create_document_runtime
from doc_uploader.models.datamodels import DataModel, GraphModel

pprint = PrettyPrinter().pprint


def test_graphmodel_with_extra_fields():
    mock_document = create_document_runtime(
        contents="hello world",
        uid="hello-0",
        relations=[
            {"doc_id": "hello-1", "rel_type": "LINK"},
            {"doc_id": "hello-2", "rel_type": "LINK"},
        ],
        doc_type="document",
        tags=set(["tag1", "tag2"]),
        authors=set(["someone1", "someone2"]),
    )
    graphmodel = GraphModel(document=mock_document)

    expected_model = DataModel(
        uid="hello-0",
        entity_type="document",
        relations=[
            {"doc_id": "hello-1", "rel_type": "LINK"},
            {"doc_id": "hello-2", "rel_type": "LINK"},
        ],
        contents="hello world",
        fields={"tags": set(["tag1", "tag2"]), "authors": set(["someone1", "someone2"])},
    )
    pprint(graphmodel.dataobj)
    assert graphmodel.dataobj == expected_model


def test_graphmodel_empty_fields():
    mock_document = create_document_runtime(
        contents="hello world",
        uid="hello-0",
        relations=[],
        doc_type="document",
    )
    graphmodel = GraphModel(document=mock_document)

    expected_model = DataModel(
        uid="hello-0",
        entity_type="document",
        relations=[],
        contents="hello world",
        fields={},
    )

    assert graphmodel.dataobj == expected_model
