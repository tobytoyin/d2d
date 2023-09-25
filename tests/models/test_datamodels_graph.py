from doc_uploader.doc_handlers.mock import mock_creator
from doc_uploader.models.datamodels import GraphModel


def test_graphmodel_with_extra_fields():
    mock_document = mock_creator(
        content="hello world",
        id="hello-0",
        relations=set(["hello-1", "hello-2"]),
        doc_type="document",
        tags=set(["tag1", "tag2"]),
        authors=set(["someone1", "someone2"]),
    )
    graphmodel = GraphModel(document=mock_document)

    expected = {
        "entity_type": "document",
        "id": "hello-0",
        "relations": set(["hello-1", "hello-2"]),
        "tags": set(["tag1", "tag2"]),
        "authors": set(["someone1", "someone2"]),
    }

    assert graphmodel.dict == expected


def test_graphmodel_empty_fields():
    mock_document = mock_creator(
        content="hello world",
        id="hello-0",
        relations=set(["hello-1", "hello-2"]),
        doc_type="document",
    )
    graphmodel = GraphModel(document=mock_document)

    expected = {
        "entity_type": "document",
        "id": "hello-0",
        "relations": set(["hello-1", "hello-2"]),
    }

    assert graphmodel.dict == expected
