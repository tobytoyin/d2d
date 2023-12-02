import pytest

from d2d.api.documents_dispatcher import DocumentServicesDispatcher
from d2d.contracts.documents import Document
from d2d.plugins.neo4j.document_to_db import DocumentToNeo4J


@pytest.fixture
def document():
    return Document(uid="test_documents_dispatcher")


def test_doc_to_graph_route(document):
    # with factory approach
    _ = DocumentServicesDispatcher.service_runner(
        document,
        plugin_name="neo4j",
        service_name="update_or_create_linked_documents",
    )

    # with service object apporach
    _ = DocumentServicesDispatcher.service_runner(
        document,
        service_catalog=DocumentToNeo4J(),
        service_name="update_or_create_linked_documents",
    )
