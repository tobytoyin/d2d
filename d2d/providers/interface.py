from typing import (
    Any,
    Callable,
    Generic,
    Literal,
    Protocol,
    TypeAlias,
    TypeVar,
    runtime_checkable,
)

from d2d.contracts.interfaces import ProviderSourceMetaHandlers, ProviderTaskHandlers
from d2d.contracts.payload import SourceDict

T = TypeVar("T")
TaskResultDict: TypeAlias = dict[str, Any]
TaskFunction: TypeAlias = Callable[[T], TaskResultDict]


@runtime_checkable
class SourceTextTasks(ProviderTaskHandlers[str, TaskResultDict], Protocol):
    """Interface for Storing Text-related Tasks

    :param Protocol: _description_
    :type Protocol: _type_
    """

    # all function in this interface follows TaskSignature
    @staticmethod
    def summary(_: str) -> TaskResultDict:
        ...
