# from pytest import fixture

# from doc_uploader.doc_handlers.factory import create_document_runtime
# from doc_uploader.models.datamodels import GraphModel
# from doc_uploader.services.db_handler.factory import get_uow


# @fixture
# def graphmodel():
#     mock_document = create_document_runtime(
#         contents="hello world",
#         uid="hello-0",
#         relations=set(["hello-1", "hello-2"]),
#         doc_type="document",
#         tags=set(["tag1", "tag2"]),
#         authors=set(["someone1", "someone2"]),
#     )
#     return GraphModel(mock_document)


# def test_mock_uploader(graphmodel):
#     uploader = get_uow("mock")

#     res1, res2 = uploader(graphmodel)
#     assert res1 == 5
#     assert res2 == 2
