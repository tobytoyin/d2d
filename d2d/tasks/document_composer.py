import logging

from pydantic import ValidationError

from d2d.contracts.documents import Summary


def summary_composer(d: dict) -> Summary:
    try:
        return Summary.model_validate(d)
    except ValidationError as e1:
        logging.warning(e1)
        logging.warning("summary input is not compatible")
        return Summary()
