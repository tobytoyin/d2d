from __future__ import annotations

import logging

from pydantic import ValidationError

from d2d.contracts.documents import DocumentComponent, Summary
from d2d.providers.interface import ProviderTaskHandlers

from ..types import IncompatiblePayload


# We use these functions to convert the JSON/ dict objects returned from
# different Prvoiders' functions to its equalavent Pydantic model
def summary_adapter(d: dict) -> Summary:
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


class TaskFunctionsAdapters(ProviderTaskHandlers[dict, DocumentComponent]):
    """Mapper between provider tasks functions to the eqv pydantic object convertors

    :param ProviderInterface: _description_
    :type ProviderInterface: _type_
    """

    summary = summary_adapter
