from pytest import fixture

from doc_uploader.doc_handlers.mock import mock_creator
from doc_uploader.models.datamodels import GraphModel
from doc_uploader.services.uploader import Uploader


@fixture
def graphmodel():
    mock_document = mock_creator(
        content="hello world",
        id="hello-0",
        relations=set(["hello-1", "hello-2"]),
        doc_type="document",
        tags=set(["tag1", "tag2"]),
        authors=set(["someone1", "someone2"]),
    )
    return GraphModel(mock_document)


def test_mock_uploader(graphmodel):
    uploader = Uploader()

    res1, res2 = uploader.mock_uploader(graphmodel)
    assert res1 == 5
    assert res2 == 2
