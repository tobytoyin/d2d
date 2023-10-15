from abc import ABC, abstractmethod
from typing import Generic, Protocol, Set, TypeVar

from doc_uploader.contracts.document import Document
from doc_uploader.contracts.source import Source


class ImageRefExtractor(Protocol):
    """This protocol extracts the reference of image and create Source for each

    :param Protocol: _description_
    :type Protocol: _type_
    :param Generic: _description_
    :type Generic: _type_
    """

    document: Document

    @abstractmethod
    def image_sources(self) -> Set[Source]:
        """Method to extract ImageSource from DocumentSource"""
        ...
