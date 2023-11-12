from io import IOBase
from typing import Any, Callable, Literal, Protocol, TypeAlias

from d2d.contracts.payload import SourcePayloadDict


class ProviderInterface(Protocol):
    """
    A Provider can implement a package by implement at least one type of Protocol
    - SourceTextTasks - tasks that provides a text to result implementation
    - SourceIO - tasks that provides a read to text implementation

    :param Protocol: _description_
    :type Protocol: _type_
    """


class SourceTextTasks(ProviderInterface):
    """Interface for Storing Text-related Tasks

    :param Protocol: _description_
    :type Protocol: _type_
    """

    TaskResult: TypeAlias = dict[Literal["result"], Any]
    TaskSignature: TypeAlias = Callable[[str], TaskResult]

    # all function in this interface follows TaskSignature
    summary = TaskSignature


class SourceIO(ProviderInterface):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    source_text = Callable[[SourcePayloadDict], str]
