from .document_to_db import DocumentToNeo4J

doc_to_n4j = DocumentToNeo4J()


class ServiceCatalog:
    update_or_create_document = doc_to_n4j.update_or_create_document
    delete_document = doc_to_n4j.delete_document
