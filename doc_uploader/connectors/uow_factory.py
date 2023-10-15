from ..protocols._document_to_db import DocumentToDB
from .endpoints import ConnectionEndpoints
from .mock.services.doc_to_db import MockHandler


class ConnectorsServiceCatalog:
    @classmethod
    def document_to_database(cls, dst: ConnectionEndpoints) -> DocumentToDB:
        endpoints = {
            "mock": MockHandler,
        }
        return endpoints.get(dst)
