from d2d.tasks.document_composer import DocumentComposer

from .payload_fixtures import *


def test_valid_payload(valid_payload):
    documents = DocumentComposer().run(valid_payload)

    print(list(documents))
