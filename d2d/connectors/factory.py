from .mock.services.session import MockConnector
from .neo4j.services.session import Neo4JConnector

# class ConnectorsContainer(FactoryRegistry):
#     _map = {}
#     import_pattern = "connectors/providers/*.py"


def get_connector(name: str, *args, **kwargs):
    map_ = {
        "neo4j": Neo4JConnector,
        "mock": MockConnector,
    }
    conn = map_.get(name)(*args, **kwargs)
    return conn
