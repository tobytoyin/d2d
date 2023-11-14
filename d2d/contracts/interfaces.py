from typing import Callable, Generic, Optional, Protocol, TypeVar, runtime_checkable

from d2d.contracts.payload import SourcePayloadDict

T = TypeVar("T", bound=Callable)


@runtime_checkable
class ProviderTaskHandlers(Protocol, Generic[T]):
    """
    A Provider can implement a package by implement at least one type of Protocol

    :param Protocol: _description_
    :type Protocol: _type_
    """

    summary: T


@runtime_checkable
class ProviderSourceMetaHandlers(Protocol):
    """Responsible to convert source payload into internal IO

    :param Protocol: _description_
    :type Protocol: _type_
    """

    @staticmethod
    def source_text(payload: SourcePayloadDict) -> str:
        """function to interact with 3rd party source and return string contents

        :param payload: _description_
        :type payload: SourcePayloadDict
        :return: _description_
        :rtype: str
        """
        ...

    @staticmethod
    def uid_gen(payload: SourcePayloadDict) -> str:
        """function to interact with 3rd party source and return string UID

        :param payload: _description_
        :type payload: SourcePayloadDict
        :return: _description_
        :rtype: str
        """
        ...
