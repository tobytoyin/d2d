from abc import ABC, abstractmethod
from typing import Set

from ._source import DocumentSource, ImageSource


class ImageRefExtractor(ABC):
    def __init__(self, source: DocumentSource) -> None:
        self._source = source

    @abstractmethod
    def _reference_extractor(self) -> Set[ImageSource]:
        """Method to extract ImageSource from DocumentSource"""
        ...

    def image_sources(self):
        ...
