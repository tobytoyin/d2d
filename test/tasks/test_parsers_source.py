import logging
from pathlib import Path

import pydantic
import pytest

from d2d.tasks.parsers import IncompatiblePayload, source_parser


def test_source_parser():
    payload = {"path": "hello.txt"}

    source = source_parser(payload)

    assert source == payload


def test_source_parser_returns_valid_keys_only():
    payload = {
        "path": ".",
        "options": {"option1": "value1"},
        "invalid": "invalid keyed value",
    }

    source = source_parser(payload)

    del payload["invalid"]
    assert source == payload


def test_source_parser_invalid():
    payload = {"url": "https://www.cloud.com/my-file.txt"}

    with pytest.raises(IncompatiblePayload):
        _ = source_parser(payload)
