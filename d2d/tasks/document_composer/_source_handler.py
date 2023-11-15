import logging
from functools import cache
from typing import Generator

from pydantic import ValidationError

from d2d.contracts.payload import Source, SourceDict, SourceHandler
from d2d.providers.factory import get_source_handling_provider
from d2d.tasks.common import transform_function_with_options


def filter_and_validate_sources(
    sources: list[SourceDict],
) -> Generator[Source, None, None]:
    """Given a list of sources JSON, filter out all the valid sources

    :param sources: _description_
    :type sources: list[SourceDict]
    :yield: _description_
    :rtype: _type_
    """

    for i, s in enumerate(sources):
        try:
            yield Source.model_validate(s)

        except ValidationError:
            logging.warning("sources[%d] is not compatible", i)
            continue


@cache
def get_source_text(source: Source, handler_payload: SourceHandler) -> str:
    # converting between Source to dict to allow cache,
    # this allow function to only interact with external source once to get the content

    # NOTE - maybe using a singleton class to cache the text with a map instead?

    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.source_text, handler_payload.options)
    return fn(source.model_dump())


@cache
def get_source_uid(source: Source, handler_payload: SourceHandler) -> str:
    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.uid_gen, handler_payload.options)
    return fn(source.model_dump())
