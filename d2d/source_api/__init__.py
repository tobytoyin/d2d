from __future__ import annotations

import logging
from collections import namedtuple
from functools import cached_property
from typing import Generator

from pydantic import ValidationError

import d2d.contracts.exceptions as exc
from d2d.contracts.payload import (
    JobPayload,
    Source,
    SourceMetadata,
    SourceMetadataModel,
    SourceSpec,
)
from d2d.providers.factory import get_source_handling_provider
from d2d.tasks.common import transform_function_with_options

SourceMetaItems = namedtuple("SourceMetaItems", "source_metadata source_text")


class SourceLoader:
    """
    SourceHandler (SourceAPI) has a simple purpose:
    - it takes it a `Source` configuration object
    - read in the source contents, metadata
    - and generates uid for the source
    """

    def __init__(self, source: Source, spec: SourceSpec) -> None:
        self.source = source
        self.spec = spec

    @property
    def provider(self):
        return get_source_handling_provider(provider_name=self.spec.provider)

    @cached_property
    def source_text(self) -> str:
        # converting between Source to dict to allow cache,
        # this allow function to only interact with external source once to get the content

        # NOTE - maybe using a singleton class to cache the text with a map instead?

        fn = transform_function_with_options(
            self.provider.source_text,
            self.spec.options,
        )
        return fn(self.source.model_dump())

    @cached_property
    def source_metadata(self) -> SourceMetadataModel:
        fn = transform_function_with_options(
            self.provider.metadata,
            self.spec.options,
        )

        return SourceMetadataModel(**fn(self.source.model_dump()))

    @property
    def source_uid(self) -> str:
        return self.source_metadata.uid
