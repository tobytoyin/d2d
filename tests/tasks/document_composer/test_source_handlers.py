import logging

from d2d.contracts.payload import Source, SourceSpec
from d2d.tasks.document_composer._source_handler import get_source_contents

from ..payload_fixtures import *


### Assuming upstream validates SourceHanlder
### Proceed to get the text from source
### Note - options are not tested herein, they are tested in common functionality
def test_get_source_contents():
    handler_payload = SourceSpec(provider="mock")
    source = Source(path="dummy.txt")  # type: ignore
    reader = list(get_source_contents(source, handler_payload))[0]
    assert reader["raw"] == "mock io contents"
