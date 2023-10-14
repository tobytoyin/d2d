from pathlib import Path

from pytest import fixture

from doc_uploader.apis.sources_to_documents import SourcesToDocuments
from doc_uploader.contracts.document import DocUID, Document
from doc_uploader.contracts.source import ObjectSource


@fixture
def random_source():
    # create 10 randoms doc
    return [ObjectSource(path=Path("."), source_type="mock") for _ in range(10)]


def test_endpoint_yield_correct_type(random_source):
    endpoint = SourcesToDocuments(sources=random_source)
    docs_iter = endpoint.docs_iter()
    doc_instance = list(docs_iter)[0]

    # 1st element is the index
    assert isinstance(doc_instance[0], DocUID)
    # 2nd element is the docuemnt
    assert isinstance(doc_instance[1], Document)


def test_document_parser_batch(random_source):
    endpoint = SourcesToDocuments(sources=random_source)
    docs_batch = list(endpoint.docs_batch(batch_size=5))

    assert len(docs_batch) == 2  # 10 docs with 5  batch = 2 docs

    # test on the first batch
    batch_1 = list(docs_batch[0])

    assert len(batch_1) == 5

    batch_instance = batch_1[0]

    # 1st element is the index
    assert isinstance(batch_instance[0], DocUID)
    # 2nd element is the docuemnt
    assert isinstance(batch_instance[1], Document)
