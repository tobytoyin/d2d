import logging
from functools import lru_cache
from io import IOBase
from typing import Callable

from pydantic import ValidationError

from d2d.contracts.payload import Source, SourcePayload
from d2d.providers import interface, mock

from . import types


def source_validate(d: SourcePayload) -> SourcePayload:
    try:
        # check if dict payload is validat with model
        _ = Source.model_validate(d)
        return d
    except ValidationError as e1:
        logging.warning("source input is not compatible")
        raise types.IncompatiblePayload("source input is not compatible") from e1


def get_source_text(provider_name: str, d: SourcePayload) -> str:
    source = source_validate(d)

    catalog = {"mock": mock.IOCatalog}

    provider = catalog.get(provider_name, None)

    if not provider:
        raise types.ResourceNotFound("provider not found")

    return provider.source_text(source)


@lru_cache()
def with_source_text(
    fn: interface.SourceTextTasks.TaskSignature,
) -> Callable[[str, SourcePayload], interface.SourceTextTasks.TaskResult]:
    """source_io decorator to cache and wrap around other task functions.

    This allows only runtime defined or non-packaged functions to follow the\
    same interface when using source_io implemented by other providers

    :param fn: _description_
    :type fn: function
    """

    def _wrapper(
        provider_name: str, d: SourcePayload
    ) -> interface.SourceTextTasks.TaskResult:
        io_string = get_source_text(provider_name, d)
        return fn(io_string)

    return _wrapper
