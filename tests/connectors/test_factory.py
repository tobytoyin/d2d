from d2d.connectors.factory import get_connector
from d2d.connectors.mock.services.session import MockConnector
from d2d.connectors.neo4j.services.session import Neo4JConnector


def test_get_mock():
    connector = get_connector("mock")
    assert isinstance(connector, MockConnector)
