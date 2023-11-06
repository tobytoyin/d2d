import logging
from pathlib import Path

import pydantic
import pytest

from d2d.tasks.parsers import IncompatiblePayload, source_parser


def test_source_parser():
    payload = {"path": "hello.txt"}

    source = source_parser(payload)

    assert source.path == Path("hello.txt")


def test_source_parser_path_is_url():
    payload = {"path": "https://www.cloud.com/my-file.txt"}

    source = source_parser(payload)

    assert source.path == Path("https://www.cloud.com/my-file.txt")
    logging.debug(source)


def test_source_parser_accept_options():
    payload = {
        "path": ".",
        "options": {"option1": "value1"},
    }

    source = source_parser(payload)

    assert source.options == {"option1": "value1"}


def test_source_parser_invalid():
    payload = {"url": "https://www.cloud.com/my-file.txt"}

    with pytest.raises(IncompatiblePayload):
        _ = source_parser(payload)
