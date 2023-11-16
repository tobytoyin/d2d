import d2d.contracts.exceptions as exc
from d2d.tasks.document_composer import DocumentComposer

from .payload_fixtures import *


def test_doc_composer_valid_payload(valid_payload):
    documents = DocumentComposer().run(valid_payload)
    assert len(tuple(documents)) == 2


def test_doc_composer_invalid_payload_sources(invalid_payload_sources):
    documents = DocumentComposer().run(invalid_payload_sources)
    assert len(tuple(documents)) == 1


def test_doc_composer_invalid_payload(invalid_payload):
    documents = DocumentComposer().run(invalid_payload)

    with pytest.raises(exc.IncompatiblePayload):
        _ = tuple(documents)


def test_doc_composer_payload_with_options(payload_with_options):
    documents = DocumentComposer().run(payload_with_options)
    assert len(tuple(documents)) == 3


def test_doc_composer_payload_with_options_unpack(payload_with_options_unpacked):
    documents = DocumentComposer().run(payload_with_options_unpacked)
    assert len(tuple(documents)) == 3
