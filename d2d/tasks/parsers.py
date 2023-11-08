import logging

from pydantic import ValidationError

from d2d.contracts.documents import Summary

from .types import IncompatiblePayload


def summary_composer(d: dict[str, str]) -> Summary:
    """Convert a input dictionary into structural Summary

    :param d: payload object
    :type d: dict[str, str]
    :return: Summary object parsed from input dictionary
    :rtype: Summary
    """
    try:
        return Summary.model_validate(d)
    except ValidationError:
        err = IncompatiblePayload("summary input is not compatible")
        logging.warning(err)
        return Summary()
