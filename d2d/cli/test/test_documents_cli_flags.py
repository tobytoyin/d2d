from argparse import ArgumentParser

import pytest

from d2d.cli.documents_to_graph import _Flags


@pytest.fixture
def base_parser():
    return ArgumentParser(prog="TestParser")


def test_json_flag(base_parser):
    json = '{"key": "hello"}'

    _Flags.json(base_parser)
    print(base_parser.parse_args(["--json", json]))


def test_files_flag(base_parser):
    _Flags.files(base_parser)
    print(base_parser.parse_args(["--files", "file1.txt", "file2.txt"]))


def test_tasks(base_parser):
    _Flags.tasks(base_parser)

    args = base_parser.parse_args(
        [
            "--task",
            'task1={"option": 1}',
            'task2={"option": 2}',
        ]
    )

    print(args)


def test_document_servicess(base_parser):
    _Flags.document_services(base_parser)

    args = base_parser.parse_args(
        [
            "--document_services",
            '{"option": 1}',
            '{"option": 2}',
        ]
    )

    assert len(args.document_services) == 2
    assert args.document_services[0] == {"option": 1}
