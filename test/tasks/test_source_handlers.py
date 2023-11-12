import logging
from pathlib import Path

import pydantic
import pytest

from d2d.contracts.payload import Source
from d2d.tasks import types
from d2d.tasks.source_handler import get_source_text, get_source_uid, source_validate


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
    payload = Source.model_validate(valid_payload)
    reader = get_source_text(provider_name="mock", d=payload)
    assert reader == "mock io contents"


def test_source_io_no_provider(valid_payload):
    payload = Source.model_validate(valid_payload)
    with pytest.raises(types.ResourceNotFound):
        _ = get_source_text(provider_name="none", d=payload)


def test_source_uid(valid_payload):
    payload = Source.model_validate(valid_payload)
    uid = get_source_uid(provider_name="mock", d=payload)
    assert uid == "mock-id-000"
