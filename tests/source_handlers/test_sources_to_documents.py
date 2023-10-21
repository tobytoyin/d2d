from pathlib import Path

from pytest import fixture

from d2d.contracts.document import DocUID, Document
from d2d.contracts.source import Source
from d2d.source_handlers.sources_to_documents import (
    sources_to_documents,
    sources_to_documents_batches,
)


@fixture
def random_source():
    # create 10 randoms doc
    return [Source(path=Path("."), source_type="mock") for _ in range(10)]


def test_endpoint_yield_correct_type(random_source):
    docs_iter = sources_to_documents(sources=random_source)
    doc_instance = list(docs_iter)[0]

    # 1st element is the index
    assert isinstance(doc_instance[0], DocUID)
    # 2nd element is the docuemnt
    assert isinstance(doc_instance[1], Document)


def test_document_parser_batch(random_source):
    docs_batch = list(sources_to_documents_batches(sources=random_source, batch_size=5))

    assert len(docs_batch) == 2  # 10 docs with 5  batch = 2 docs

    # test on the first batch
    batch_1 = list(docs_batch[0])

    assert len(batch_1) == 5

    batch_instance = batch_1[0]

    # 1st element is the index
    assert isinstance(batch_instance[0], DocUID)
    # 2nd element is the docuemnt
    assert isinstance(batch_instance[1], Document)
