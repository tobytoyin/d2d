from typing import Iterable

from doc_uploader.app.logger import setup_service_logger
from doc_uploader.connectors.factory import get_connector
from doc_uploader.connectors.uow_factory import ConnectorsServiceCatalog
from doc_uploader.contracts.document import Document

logger = setup_service_logger("app")

ENDPOINT = ConnectorsServiceCatalog.document_to_database


class DocumentToDatabase:
    def __init__(self, documents: Iterable[Document], destination: str) -> None:
        self.documents = documents
        self.destination = destination

    def run(self):
        conn = get_connector(self.destination)

        for doc in self.documents:
            logger.info("Uploading object")
            logger.info(repr(doc))

            service_uow = ENDPOINT(dst=doc.source.source_type)(doc)

            doc_res = conn.run(service_uow.update_or_create_document)
            logger.info(f"uploaded {doc_res} document to {self.destination}")

            rel_res = conn.run(service_uow.update_or_create_relationships)
            logger.info(f"created/updated {rel_res} relations for document-{doc.uid}")


if __name__ == "__main__":
    from pathlib import Path

    from doc_uploader.adapters.factory import create_document
    from doc_uploader.contracts.source import Source

    documents = [
        create_document(Source(path=Path("."), source_type="mock")) for _ in range(5)
    ]

    service = DocumentToDatabase(documents=documents, destination="mock")
    service.run()
