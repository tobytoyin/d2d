from enum import Enum


class ConnectionEndpoints(str, Enum):
    NEO4J = "neo4j"
    MOCK = "mock"
