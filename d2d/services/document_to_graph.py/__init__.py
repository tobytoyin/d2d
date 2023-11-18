from d2d.contracts.documents import Document
from d2d.plugins.neo4j.document_to_db import DocumentToNeo4J


class DocumentToGraph:
    def run(self, document: Document):
        process = DocumentToNeo4J()
        process.update_or_create_document
