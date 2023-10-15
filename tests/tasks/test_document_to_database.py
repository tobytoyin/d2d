# example usage
from pathlib import Path

from doc_uploader.contracts.source import Source
from doc_uploader.source_handlers.sources_to_documents import sources_to_documents
from doc_uploader.tasks.document_to_database import DocumentToDatabase


def test_endpoint():
    # setup dummy sources
    sources = [Source(path=Path("."), source_type="mock") for _ in range(5)]
    documents = list(sources_to_documents(sources))

    expected_uid = [document.uid for _, document in documents]

    service = DocumentToDatabase(documents=documents, destination="mock")
    service.run()

    print(service.results)
    results = list(service.results)

    assert set(results) == set(expected_uid)
    assert len(results) == len(expected_uid)
