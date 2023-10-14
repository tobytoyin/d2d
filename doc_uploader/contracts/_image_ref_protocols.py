from abc import ABC, abstractmethod
from typing import Generic, Protocol, Set, TypeVar

from .document import DocumentContent
from .source import ImageSource

T = TypeVar("T", bound=DocumentContent, contravariant=True)


class ImageRefExtractor(Protocol, Generic[T]):
    @abstractmethod
    def image_sources(self, content: T) -> Set[ImageSource]:
        """Method to extract ImageSource from DocumentSource"""
        ...
