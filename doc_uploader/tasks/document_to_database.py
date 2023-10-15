from itertools import tee
from typing import Iterable

from doc_uploader.app.logger import setup_service_logger
from doc_uploader.connectors.catalog import ServicesCatalog
from doc_uploader.connectors.factory import get_connector
from doc_uploader.contracts._types import DocumentIterable
from doc_uploader.contracts.document import Document

logger = setup_service_logger("document_to_database")

ENDPOINT = ServicesCatalog.document_to_database


class DocumentToDatabase:
    def __init__(self, documents: DocumentIterable, destination: str) -> None:
        self.documents = documents
        self.destination = destination
        self._results = []

    def run(self):
        conn = get_connector(self.destination)

        for uid, doc in self.documents:
            logger.info(f"Uploading document-{uid}")
            logger.info(repr(doc))

            service_uow = ENDPOINT(dst=doc.source.source_type)(doc)

            doc_res = conn.run(service_uow.update_or_create_document)
            logger.info(f"uploaded {doc_res} document to {self.destination}")

            rel_res = conn.run(service_uow.update_or_create_relationships)
            logger.info(f"created/updated {rel_res} relations for document-{uid}")
            self._results.append(doc_res)

        logger.info("Process completed")

    @property
    def results(self):
        return self._results


if __name__ == "__main__":
    # example usage
    from pathlib import Path

    from doc_uploader.contracts.source import Source
    from doc_uploader.source_handlers.sources_to_documents import sources_to_documents

    sources = [Source(path=Path("."), source_type="mock") for _ in range(5)]
    documents = sources_to_documents(sources)

    service = DocumentToDatabase(documents=documents, destination="mock")
    service.run()

    print(service.results)
