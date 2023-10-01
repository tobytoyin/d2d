from collections.abc import Iterable


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


def invalid_key_fix(obj: dict, invalid_sym: str, valid_sym: str) -> dict:
    """convert invalid key symbol into a valid symbol"""
    return {k.replace(invalid_sym, valid_sym): v for k, v in obj.items()}
