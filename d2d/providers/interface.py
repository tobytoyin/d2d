from typing import Any, Callable, Generic, Literal, Protocol, TypeAlias, TypeVar

from d2d.contracts.payload import SourcePayloadDict

T = TypeVar("T")
TaskResultDict: TypeAlias = dict[Literal["result"], Any]
TaskFunction: TypeAlias = Callable[[T], TaskResultDict]


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

    # all function in this interface follows TaskSignature
    summary = TaskFunction[str]


class SourceMetaTasks(ProviderInterface):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    source_text = Callable[[SourcePayloadDict], str]
    uid_gen = Callable[[SourcePayloadDict], str]
