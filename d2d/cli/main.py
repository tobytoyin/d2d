import argparse
from functools import partialmethod

from d2d.api import DocumentsEndpoint
from d2d.cli.utils import ParseKwargs, json_type


class _Flags:
    @staticmethod
    def json(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--json",
            type=json_type,
            default=None,
            help="execute api using a JSON file",
            required=False,
        )

    @staticmethod
    def files(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--files",
            type=str,
            nargs="+",
            help="List of source assuming that only 'path' is being used.",
        )

    @staticmethod
    def sources(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--sources",
            type=json_type,
            nargs="+",
            help="List of source JSON objects",
        )

    @staticmethod
    def source_spec(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--source_spec", type=json_type)

    @staticmethod
    def tasks(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--tasks",
            action=ParseKwargs,
            nargs="*",
            help="adding task to 'tasks'. e.g. summary={...}",
        )

    @staticmethod
    def document_services(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--document_services",
            type=json_type,
            nargs="+",
            help="adding task to 'tasks'. e.g. summary={...}",
        )


class CommandLine:
    parser = argparse.ArgumentParser(prog="document_to_graph")

    _Flags.json(parser)
    _Flags.files(parser)
    _Flags.sources(parser)
    _Flags.source_spec(parser)
    _Flags.tasks(parser)
    _Flags.document_services(parser)

    @classmethod
    def get_args(cls):
        return cls.parser.parse_args()

    @classmethod
    def _handle_files_sources_flag(cls):
        if sources := cls.get_args().sources:
            return sources

        files = cls.get_args().files
        out = []
        for file in files:
            out.append({"path": file})
        return out

    @classmethod
    def construct_payload(cls):
        args = cls.get_args()

        if payload := args.json:
            return payload

        return {
            "sources": cls._handle_files_sources_flag(),
            "source_spec": args.source_spec,
            "tasks": {k: v for t in args.task for k, v in t.items()},
            "document_services": args.document_services,
        }


if __name__ == "__main__":
    args = CommandLine.construct_payload()
    _ = DocumentsEndpoint.run(args)
