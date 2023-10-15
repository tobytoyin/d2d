from doc_uploader.connectors.factory import get_connector
from doc_uploader.connectors.mock.services.session import MockConnector
from doc_uploader.connectors.neo4j.services.session import Neo4JConnector


def test_get_mock():
    connector = get_connector("mock")
    assert isinstance(connector, MockConnector)
