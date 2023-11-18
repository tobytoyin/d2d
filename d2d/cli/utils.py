import argparse
import json


def json_type(input_str):
    try:
        json.loads(input_str)
        return json.loads(input_str)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid JSON: {e}")
