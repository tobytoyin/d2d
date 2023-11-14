import logging

import pytest

from d2d.contracts.documents import Document, Summary
from d2d.contracts.payload import TaskFunctionResult
from d2d.tasks._document_composer import DocumentComposer
from d2d.tasks._taskspec_handler import (
    components_to_document,
    convert_to_document_component,
    payload_validator,
    run_tasks,
)

from .payload_fixtures import *


#### Test on taskspec_validator on handling JSON payload ####
def test_tasksepc_validator(valid_payload):
    _ = payload_validator(valid_payload)


def test_taskspec_validator_rejects(invalid_payload):
    with pytest.raises(Exception):
        _ = payload_validator(invalid_payload)


#### Test on run_tasks can execute task functions ####
def test_run_tasks(valid_payload):
    payload = payload_validator(valid_payload)
    results = list(run_tasks(payload))

    assert results[0] == TaskFunctionResult(
        source_uid="mock-id-000",
        result={"content": "hello world"},
        kind="summary",
    )
    assert len(results) == 1


def test_run_tasks_with_invalid_tasks(payload_with_invalid_task):
    payload = payload_validator(payload_with_invalid_task)
    results = list(run_tasks(payload))
    logging.info(results)

    assert len(results) == 1


def test_run_tasks_with_invalid_provider(payload_with_invalid_provider):
    payload = payload_validator(payload_with_invalid_provider)
    results = list(run_tasks(payload))
    logging.info(results)

    assert len(results) == 0


def test_run_tasks_with_duplicate_tasks(payload_with_repeated_task_indicator):
    payload = payload_validator(payload_with_repeated_task_indicator)
    results = list(run_tasks(payload))
    logging.info(results)

    # should keep the first one only
    assert len(results) == 1


def test_convert_to_document_component(valid_payload):
    payload = payload_validator(valid_payload)
    results = run_tasks(payload)
    doc_components = map(convert_to_document_component, results)
    doc_components = list(doc_components)

    assert len(doc_components) == 1
    assert doc_components[0] == Summary(content="hello world")


def test_document_composer():
    components = [Summary(content="hello world")]
    document = components_to_document(uid="100", components=components)

    expected_doc = Document(
        uid="100",
        summary=Summary(content="hello world"),
    )

    assert document == expected_doc


def test_document_composer_endpoint(valid_payload):
    document = DocumentComposer().run(valid_payload)
    expected_doc = Document(
        uid="mock-id-000",
        summary=Summary(content="hello world"),
    )
    assert document == expected_doc
