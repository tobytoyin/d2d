from typing import Any, Callable, Protocol, TypeAlias, TypeVar, runtime_checkable

from d2d.contracts.interfaces import ProviderTaskHandlers

T = TypeVar("T")
TaskResultDict: TypeAlias = dict[str, Any]
TaskFunction: TypeAlias = Callable[[T], TaskResultDict]


@runtime_checkable
class SourceTextTasks(ProviderTaskHandlers[str, TaskResultDict], Protocol):
    """Interface for Storing Text-related Tasks"""

    @staticmethod
    def summary(_: str, /) -> TaskResultDict:
        ...

    @staticmethod
    def metadata(_: str, /) -> TaskResultDict:
        ...

    # @staticmethod
    # def relations(_: str, /) -> TaskResultDict:
    #     ...
