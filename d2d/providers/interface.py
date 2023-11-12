from typing import Any, Callable, Generic, Literal, Protocol, TypeAlias, TypeVar

from d2d.contracts.interfaces import ProviderInterface
from d2d.contracts.payload import SourcePayloadDict

T = TypeVar("T")
TaskResultDict: TypeAlias = dict[str, Any]
TaskFunction: TypeAlias = Callable[[T], TaskResultDict]


class SourceTextTasks(ProviderInterface[TaskFunction[str]]):
    """Interface for Storing Text-related Tasks

    :param Protocol: _description_
    :type Protocol: _type_
    """

    # all function in this interface follows TaskSignature
    summary: TaskFunction[str]


class SourceMetaTasks(Protocol):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    source_text: Callable[[SourcePayloadDict], str]
    uid_gen: Callable[[SourcePayloadDict], str]
