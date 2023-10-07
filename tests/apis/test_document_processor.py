from pytest import fixture

from doc_uploader.apis._document_processor import DocumentParserInput, DocumentsParser
from doc_uploader.doc_processor.interfaces import Document
from doc_uploader.doc_processor.types import DocID


@fixture
def random_payload():
    # create 10 randoms doc
    return DocumentParserInput(source="mock", files=list(map(str, range(10))))


def test_document_parser_iter_document(random_payload):
    parser = DocumentsParser(random_payload)
    docs_iter = parser.docs_iter()
    doc_instance = list(docs_iter)[0]

    # 1st element is the index
    assert isinstance(doc_instance[0], DocID)
    # 2nd element is the docuemnt
    assert isinstance(doc_instance[1], Document)


def test_document_parser_batch(random_payload):
    parser = DocumentsParser(random_payload)
    docs_batch = list(parser.docs_batch(batch_size=5))

    assert len(docs_batch) == 2  # 10 docs with 5  batch = 2 docs

    # test on the first batch
    batch_1 = list(docs_batch[0])

    assert len(batch_1) == 5

    batch_instance = batch_1[0]

    # 1st element is the index
    assert isinstance(batch_instance[0], DocID)
    # 2nd element is the docuemnt
    assert isinstance(batch_instance[1], Document)
