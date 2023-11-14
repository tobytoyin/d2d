from typing import Any, Callable, Generic, Literal, Protocol, TypeAlias, TypeVar

from d2d.contracts.interfaces import ProviderTaskHandlers
from d2d.contracts.payload import SourcePayloadDict

T = TypeVar("T")
TaskResultDict: TypeAlias = dict[str, Any]
TaskFunction: TypeAlias = Callable[[T], TaskResultDict]


class SourceTextTasks(ProviderTaskHandlers[TaskFunction[str]]):
    """Interface for Storing Text-related Tasks

    :param Protocol: _description_
    :type Protocol: _type_
    """

    # all function in this interface follows TaskSignature
    summary: TaskFunction[str]
