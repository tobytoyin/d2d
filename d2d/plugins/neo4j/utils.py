from typing import Iterable


# neo4j needs " to be \\" within the contents
def escape_double_quote(s: str):
    return s.replace('"', '\\"')


def no_quotes_object(obj: dict) -> str:
    """convert python dict object to object without quoted key

    Example:
    old = {"key": "value"}
    new = no_quotes_object(old)
    # new becomes '{key: "value"}'
    """

    prop_strings = []
    for k, v in obj.items():
        # ensure objects are wraped with "" but not "[...]" the iterable object
        if not isinstance(v, str) and isinstance(v, Iterable):
            v = [f"{item}" for item in v]
            prop_strings.append(f"{k}: {v}")
        else:
            prop_strings.append(f'{k}: "{v}"')

    return "{" + ",".join(prop_strings) + "}"
