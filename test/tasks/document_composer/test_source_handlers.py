import pytest

from d2d.contracts.payload import Source, SourceHandler
from d2d.tasks.document_composer._source_handler import (
    filter_and_validate_sources,
    get_source_text,
    get_source_uid,
)


@pytest.fixture
def valid_sources():
    # under "sources: [...]"
    return [{"path": "hello1.txt"}, {"path": "hello2.txt"}]


@pytest.fixture
def partial_valid_sources():
    return [{"path": "hello1.txt"}, {"paths": "hello2.txt"}]


def test_valid_sources(valid_sources):
    sources = filter_and_validate_sources(valid_sources)
    assert len(list(sources)) == 2


def test_partial_valid_sources(partial_valid_sources):
    sources = filter_and_validate_sources(partial_valid_sources)
    assert len(list(sources)) == 1


### Assuming upstream validates SourceHanlder
### Proceed to get the text from source
### Note - options are not tested herein, they are tested in common functionality
def test_get_source_text():
    handler_payload = SourceHandler(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = get_source_text(source, handler_payload)
    assert reader == "mock io contents"


def test_source_uid():
    handler_payload = SourceHandler(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = get_source_uid(source, handler_payload)
    assert reader == "mock-id-000"
