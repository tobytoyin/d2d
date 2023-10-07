from pprint import PrettyPrinter

from doc_uploader.doc_handlers.factory import create_document_runtime
from doc_uploader.doc_handlers.interfaces import RelationProps
from doc_uploader.models.factory import create_graph_model

pprint = PrettyPrinter().pprint


def test_graphmodel_with_extra_fields():
    mock_document = create_document_runtime(
        contents="hello world",
        uid="hello-0",
        relations=[
            {"rel_uid": "hello-1", "rel_type": "LINK", "properties": {}},
            {"rel_uid": "hello-2", "rel_type": "LINK", "properties": {}},
        ],
        doc_type="document",
        tags=set(["tag1", "tag2"]),
        authors=set(["someone1", "someone2"]),
    )
    graphmodel = create_graph_model(mock_document)

    assert graphmodel.uid == "hello-0"
    assert graphmodel.contents == "hello world"
    assert graphmodel.fields["tags"] == set(["tag1", "tag2"])
    assert graphmodel.fields["authors"] == set(["someone1", "someone2"])
    assert graphmodel.node_type == "document"
    assert isinstance(graphmodel.relations[0], RelationProps)


# def test_graphmodel_empty_fields():
#     mock_document = create_document_runtime(
#         contents="hello world",
#         uid="hello-0",
#         relations=[],
#         doc_type="document",
#     )
#     graphmodel = GraphModel(document=mock_document)

#     expected_model = DataModel(
#         uid="hello-0",
#         entity_type="document",
#         relations=set([]),
#         contents="hello world",
#         fields={},
#     )

#     assert graphmodel.dataobj == expected_model
