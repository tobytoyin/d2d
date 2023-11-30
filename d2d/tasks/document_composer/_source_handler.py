from __future__ import annotations

import logging
from collections import namedtuple
from functools import cache
from typing import Generator

from pydantic import ValidationError

import d2d.contracts.exceptions as exc
from d2d.contracts.payload import JobPayload, Source, SourceMetadata, SourceSpec
from d2d.providers.factory import get_source_handling_provider
from d2d.tasks.common import transform_function_with_options

SourceMetaItems = namedtuple("SourceMetaItems", "source_metadata source_text")


@cache
def _get_source_text(source: Source, handler_payload: SourceSpec) -> str:
    # converting between Source to dict to allow cache,
    # this allow function to only interact with external source once to get the content

    # NOTE - maybe using a singleton class to cache the text with a map instead?

    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.source_text, handler_payload.options)
    return fn(source.model_dump())


@cache
def _get_source_metadata(source: Source, handler_payload: SourceSpec) -> SourceMetadata:
    provider_name = handler_payload.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.metadata, handler_payload.options)
    return fn(source.model_dump())


def get_source_contents(source: Source, spec: SourceSpec) -> SourceMetaItems:
    provider_name = spec.provider
    provider = get_source_handling_provider(provider_name=provider_name)

    fn = transform_function_with_options(provider.loader, spec.options)
    respond = fn(source.model_dump())

    # just returning source_text and source_uid from a single function
    source_text = respond["raw"]
    del respond["raw"]
    source_metadata = respond
    return SourceMetaItems(source_metadata, source_text)
