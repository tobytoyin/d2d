import logging

from d2d.contracts.payload import Source, SourceMetadataModel, SourceSpec
from d2d.source_api import SourceAPI


### Assuming upstream validates SourceHanlder
### Proceed to get the text from source
### Note - options are not tested herein, they are tested in common functionality
def test_source_text():
    spec = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore

    sourceapi = SourceAPI(source=source, spec=spec)
    result = sourceapi.source_text
    logging.debug(result)
    assert result == "mock io contents"


def test_source_metadata():
    spec = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore

    sourceapi = SourceAPI(source=source, spec=spec)
    result = sourceapi.source_metadata
    logging.debug(result)

    assert isinstance(result, SourceMetadataModel)
    assert result.uid == "dummy"
    assert result.createdTime != ""
