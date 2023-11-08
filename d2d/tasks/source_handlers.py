import logging
from functools import lru_cache
from io import IOBase
from typing import Any, Callable

from pydantic import ValidationError

from d2d.contracts.source import Source, SourcePayload
from d2d.providers import mock
from d2d.providers.interface import SourceTextTasks

from .types import IncompatiblePayload, ResourceNotFound


def source_validate(d: SourcePayload) -> SourcePayload:
    try:
        # check if dict payload is validat with model
        _ = Source.model_validate(d)
        return d
    except ValidationError as e1:
        logging.warning("source input is not compatible")
        raise IncompatiblePayload("source input is not compatible") from e1


def get_source_io(provider_name: str, d: SourcePayload) -> IOBase:
    source = source_validate(d)

    catalog = {"mock": mock.IOCatalog}

    provider = catalog.get(provider_name, None)

    if not provider:
        raise ResourceNotFound("provider not found")

    return provider.source_io(source)


@lru_cache()
def with_source_io(
    fn: SourceTextTasks.TaskSignature,
) -> Callable[[str, SourcePayload], SourceTextTasks.TaskResult]:
    """source_io decorator to cache and wrap around other task functions.

    This allows only runtime defined or non-packaged functions to follow the\
    same interface when using source_io implemented by other providers

    :param fn: _description_
    :type fn: function
    """

    def _wrapper(provider_name: str, d: SourcePayload) -> SourceTextTasks.TaskResult:
        io_string = get_source_io(provider_name, d).read()
        return fn(io_string)

    return _wrapper
