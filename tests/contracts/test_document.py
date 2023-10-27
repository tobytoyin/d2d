import pytest

from d2d.contracts.document import *

# These tests ensure new contracts of the Document's BaseModels
# won't be broken


def test_document_content_schema():
    fields = DocContent.model_fields.keys()

    assert "contents" in fields
    assert "bytes" in fields


def test_doc_uid_type():
    # test correct subtyping
    assert issubclass(DocUID, str)
    assert issubclass(DocUID, DocumentComponent)

    # test correct usage
    assert DocUID("test-id") == "test-id"


def test_doc_summary_type():
    # test correct subtyping
    assert issubclass(DocSummary, str)
    assert issubclass(DocSummary, DocumentComponent)

    # test correct usage
    assert DocUID("test summary") == "test summary"


def test_keywords():
    # test correct subtyping
    assert issubclass(DocKeywords, set)
    assert issubclass(DocKeywords, DocumentComponent)

    # test correct usage
    assert DocKeywords(["key1", "key2", "key1"]) == set(["key1", "key2"])


def test_metadata_contract():
    fields = DocMetadata.model_fields.keys()

    assert "doc_type" in fields
    assert "properties" in fields

    # test usages
    metadata1 = DocMetadata(doc_type="test-type")
    assert metadata1.doc_type == "test-type"
    assert metadata1.properties == {}

    metadata2 = DocMetadata(doc_type="test-type-2", properties={"k1": "v1"})
    assert metadata2.doc_type == "test-type-2"
    assert metadata2.properties == {"k1": "v1"}


def test_relation_contract():
    fields = DocRelation.model_fields.keys()

    assert "rel_uid" in fields
    assert "rel_type" in fields
    assert "properties" in fields


###### DocRelations Tests ######
def test_relationships_contract():
    # test correct subtyping
    assert issubclass(DocRelations, set)
    assert issubclass(DocRelations, DocumentComponent)


def test_relationships_rejects_wrong_types():
    with pytest.raises(TypeError):
        DocRelations("incorrect input type")  # type: ignore

    with pytest.raises(TypeError):
        DocRelations(["incorrect element type"])  # type: ignore


def test_relationships_usage():
    # test proper set creation
    rel1_1 = DocRelation(rel_uid=DocUID("1"), rel_type="test")
    rel1_2 = DocRelation(rel_uid=DocUID("1"), rel_type="test")
    rel2 = DocRelation(rel_uid=DocUID("2"), rel_type="test")

    relations = DocRelations([rel1_1, rel1_2, rel2])
    assert isinstance(relations, set)
    assert len(relations) == 2

    # test empty set creation
    relations = DocRelations()
    assert relations == set()
