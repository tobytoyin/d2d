import pytest

from d2d.api.documents import DocumentsEndpoint


@pytest.fixture
def payload():
    return {
        "sources": [{"path": "test_document_1.txt"}, {"path": "test_document_2.txt"}],
        "source_spec": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
        },
        "document_services": [
            {"plugin_name": "neo4j", "service_name": "update_or_create_document"}
        ],
    }


def test_payload_endpoint(payload):
    _ = DocumentsEndpoint.run(payload)
