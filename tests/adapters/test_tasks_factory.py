import io
from pathlib import Path

import pytest

from d2d.adapters.factory import get_adapter_service
from d2d.contracts import document
from d2d.contracts.source import Source

# Below tests ensures that the factory functions for returning the sourceTasks
# adapter's functions are working properly


@pytest.fixture
def source():
    return Source(path=Path("."), source_type="mock_type")


def test_source_io_getter(source):
    service = get_adapter_service(adapter_name="mock_all", service_name="source_io")
    result = service(source)

    assert isinstance(result, io.IOBase)


def test_links_getter(source):
    service = get_adapter_service(adapter_name="mock_all", service_name="links")
    result = service(source)

    assert isinstance(result, document.DocRelations)


def test_metadata_getter(source):
    service = get_adapter_service(adapter_name="mock_all", service_name="metadata")
    result = service(source)

    assert isinstance(result, document.DocMetadata)


def test_summary_getter(source):
    service = get_adapter_service(adapter_name="mock_all", service_name="summary")
    result = service(source)

    assert isinstance(result, document.DocSummary)


def test_keywords_getter(source):
    service = get_adapter_service(adapter_name="mock_all", service_name="keywords")
    result = service(source)

    assert isinstance(result, document.DocKeywords)


## Test if ServiceCatalog is partially implemented
def test_partial_catalog_no_task_to_get(source):
    with pytest.raises(AttributeError):
        _ = get_adapter_service(adapter_name="mock_partial", service_name="links")
