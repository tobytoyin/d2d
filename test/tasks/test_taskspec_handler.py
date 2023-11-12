import pytest

from d2d.contracts.documents import Summary
from d2d.contracts.payload import TaskFunctionResult
from d2d.tasks.taskspec_handler import (
    convert_to_document_component,
    payload_validator,
    run_tasks,
)


@pytest.fixture
def valid_spec():
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def invalid_spec():
    return {
        "sources": {
            "path": ".",
        },
        "tasks": {
            "source_reader": {"provider": "mock"},
            "summary": {"provider": "mock"},
        },
    }


@pytest.fixture
def extra_invalid_tasks():
    return {
        "source": {
            "path": ".",
        },
        "source_reader": {"provider": "mock"},
        "tasks": {
            "summary": {"provider": "mock"},
            "invalid": {"provider": "none"},
        },
    }


def test_tasksepc_validator(valid_spec):
    _ = payload_validator(valid_spec)


def test_taskspec_validator_rejects(invalid_spec):
    with pytest.raises(Exception):
        _ = payload_validator(invalid_spec)


def test_run_tasks(valid_spec):
    results = list(run_tasks(valid_spec))

    assert results[0] == TaskFunctionResult(
        result={"content": "hello world"},
        kind="summary",
    )
    assert len(results) == 1


def test_convert_to_document_component(valid_spec):
    results = run_tasks(valid_spec)
    doc_components = map(convert_to_document_component, results)
    doc_components = list(doc_components)

    assert len(doc_components) == 1
    assert doc_components[0] == Summary(content="hello world")
