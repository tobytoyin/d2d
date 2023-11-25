from pydantic import ValidationError

import d2d.contracts.exceptions as exc
from d2d.contracts.payload import JobPayload


def convert_structural_payload(payload: dict) -> JobPayload:
    """First contact point for the payload to get pass to the pipeline

    This converts a JSON payload into structural class object.


    :param payload: _description_
    :type payload: dict
    :return: _description_
    :rtype: SourcePayload
    """
    try:
        return JobPayload.model_validate(payload)
    except ValidationError as e:
        raise exc.IncompatiblePayload from e
