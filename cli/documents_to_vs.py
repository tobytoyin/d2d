import argparse

from d2d.api.document_to_vs import DocumentToVsAPI
from d2d.cli.utils import json_type


class CommandLine:
    parser = argparse.ArgumentParser(prog="document_to_graph")
    parser.add_argument("--json", type=json_type, default=None)
    parser.add_argument("--files", type=str, nargs="+")
    parser.add_argument("--sources", type=json_type, nargs="+")
    parser.add_argument("--source_spec", type=json_type)
    parser.add_argument(
        "--task",
        action="append",
        type=json_type,
        help="adding task to 'tasks'",
    )

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
        }


if __name__ == "__main__":
    args = CommandLine.construct_payload()
    _ = DocumentToVsAPI().async_run(args)
