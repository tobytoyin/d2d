import logging
from pathlib import Path

import pydantic
import pytest

from d2d.tasks import types
from d2d.tasks.source_handlers import get_source_text, source_validate, with_source_text


@pytest.fixture
def valid_payload():
    return {"path": "hello.txt"}


@pytest.fixture
def extra_payload():
    return {
        "path": ".",
        "options": {"option1": "value1"},
        "invalid": "invalid keyed value",
    }


@pytest.fixture
def invalid_payload():
    return {"url": "https://www.cloud.com/my-file.txt"}


def test_source_parser(valid_payload):
    payload = valid_payload
    source = source_validate(payload)
    assert source == payload


def test_source_parser_returns_valid_keys_only(extra_payload):
    payload = extra_payload

    source = source_validate(payload)

    del payload["invalid"]
    assert source == payload


def test_source_parser_invalid(invalid_payload):
    payload = invalid_payload

    with pytest.raises(types.IncompatiblePayload):
        _ = source_validate(payload)


def test_source_io(valid_payload):
    payload = valid_payload
    reader = get_source_text(provider_name="mock", d=payload)
    assert reader == "mock io contents"


def test_source_io_no_provider(valid_payload):
    payload = valid_payload
    with pytest.raises(types.ResourceNotFound):
        _ = get_source_text(provider_name="none", d=payload)


def test_with_source_io_decorator(valid_payload):
    # this can be any functions that follow providers.interface.SourceTask
    mock_task_fn = lambda s: {"result": s.upper()}

    content = with_source_text(mock_task_fn)(provider_name="mock", d=valid_payload)

    assert content == {"result": "MOCK IO CONTENTS"}
