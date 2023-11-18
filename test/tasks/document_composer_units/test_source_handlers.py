import logging

from d2d.contracts.payload import Source, SourceSpec
from d2d.tasks.document_composer._source_handler import (
    _get_source_text,
    _get_source_uid,
    payload_handler,
)

from ..payload_fixtures import *


def test_payload(valid_payload):
    """All Payload contents pass through

    :param valid_payload: _description_
    :type valid_payload: _type_
    """
    payload = payload_handler(valid_payload)
    assert len(payload.sources) == 2


def test_payload_with_invalid_sources(invalid_payload_sources):
    """Invald Payload's sources is skipped"""
    payload = payload_handler(invalid_payload_sources)
    assert len(payload.sources) == 1
    logging.info(payload)


### Assuming upstream validates SourceHanlder
### Proceed to get the text from source
### Note - options are not tested herein, they are tested in common functionality
def test_get_source_text():
    handler_payload = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = _get_source_text(source, handler_payload)
    assert reader == "mock io contents"


def test_source_uid():
    handler_payload = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = _get_source_uid(source, handler_payload)
    assert reader == "dummy"
