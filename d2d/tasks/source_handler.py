import logging
from functools import cache
from typing import Callable

from pydantic import ValidationError

from d2d.contracts.payload import Source, SourcePayload, SourcePayloadDict
from d2d.providers import interface, mock

from . import types


def source_validate(d: SourcePayloadDict) -> SourcePayloadDict:
    try:
        # check if dict payload is validat with model
        _ = Source.model_validate(d)
        return d
    except ValidationError as e1:
        logging.warning("source input is not compatible")
        raise types.IncompatiblePayload("source input is not compatible") from e1


@cache
def get_source_text(provider_name: str, d: SourcePayload) -> str:
    catalog = {"mock": mock.IOCatalog}
    provider = catalog.get(provider_name, None)

    if not provider:
        raise types.ResourceNotFound("provider not found")
    result = provider.source_text(d.model_dump())
    return result


@cache
def get_source_uid(provider_name: str, d: SourcePayload) -> str:
    catalog = {"mock": mock.IOCatalog}
    provider = catalog.get(provider_name, None)

    if not provider:
        raise types.ResourceNotFound("provider not found")
    return provider.uid_gen(d.model_dump())
