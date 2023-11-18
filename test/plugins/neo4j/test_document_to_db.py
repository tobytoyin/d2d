import pytest

import d2d.contracts.documents as doc
from d2d.plugins.neo4j.document_to_db import DocumentToNeo4J

from .utils import reset_neo4j


@pytest.fixture
def document_with_2_links():
    return doc.Document(
        uid="root",
        relations=doc.Relations(
            items=set(
                [
                    doc.Relation(rel_uid="rel1", rel_type="LINK"),
                    doc.Relation(
                        rel_uid="rel2", rel_type="LINK", properties={"k1": "v1"}
                    ),
                ]
            )
        ),
    )


def test_update_or_create_document(document_with_2_links):
    reset_neo4j()
    process = DocumentToNeo4J()
    process.update_or_create_document(document_with_2_links)

    # TODO test counts


def test_update_or_create_relations(document_with_2_links):
    reset_neo4j()
    process = DocumentToNeo4J()
    process.update_or_create_document(document_with_2_links)
    process.update_or_create_relations(document_with_2_links)


def test_delete_document(document_with_2_links):
    reset_neo4j()
    process = DocumentToNeo4J()
    process.update_or_create_document(document_with_2_links)
    process.delete_document(document_with_2_links)
