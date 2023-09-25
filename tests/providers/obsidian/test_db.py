from doc_uploader.base.db_models import GraphDocumentModel
from doc_uploader.providers.obsidian.models import *
from tests.providers.obsidian.load_test_files import *


def test_graph_doc_1(doc_with_frontmatter):
    expected = {
        'id': 'doc_with_frontmatter',
        'relations': set(),
        'node_type': 'test',
        'fields': {'name': 'my-dummy-doc'},
    }

    record = GraphDocumentModel(document=doc_with_frontmatter).record
    assert expected == record


def test_graph_doc_2(doc_without_frontmatter):
    expected = {
        'id': 'doc_without_frontmatter',
        'relations': set(),
        'node_type': 'unknown',
        'fields': {},
    }

    record = GraphDocumentModel(document=doc_without_frontmatter).record
    assert expected == record


def test_graph_doc_3(doc_with_links):
    expected = {
        'id': 'doc_with_internal_links',
        'relations': set(['document-id-1', 'document-id-2', 'document-id-3']),
        'node_type': 'test',
        'fields': {'name': 'my-dummy-doc'},
    }

    record = GraphDocumentModel(document=doc_with_links).record
    assert expected == record


def test_graph_doc_4(doc_without_links):
    expected = {
        'id': 'doc_without_internal_links',
        'relations': set(),
        'node_type': 'test',
        'fields': {'name': 'my-dummy-doc'},
    }

    record = GraphDocumentModel(document=doc_without_links).record
    assert expected == record
