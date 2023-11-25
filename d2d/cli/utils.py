import argparse
import json


def json_type(input_str):
    try:
        json.loads(input_str)
        return json.loads(input_str)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid JSON: {e}")


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value
