from typing import Callable, Generic, Optional, Protocol, TypeVar

from d2d.contracts.payload import SourcePayloadDict

T = TypeVar("T", bound=Callable)


class ProviderTaskHandlers(Protocol, Generic[T]):
    """
    A Provider can implement a package by implement at least one type of Protocol

    :param Protocol: _description_
    :type Protocol: _type_
    """

    summary: T


class ProviderSourceMetaHandlers(Protocol):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    source_text: Callable[[SourcePayloadDict], str]
    uid_gen: Callable[[SourcePayloadDict], str]
