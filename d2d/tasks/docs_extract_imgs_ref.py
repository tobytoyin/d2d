import inspect
from typing import List, Sequence, Type

from d2d.contracts.document import Document
from d2d.contracts.source import Source
from d2d.protocols._extract_image_sources import ImageRefExtractor


# Take all the Documents at the beginning and convert them into iterator
class DocumentsToImageSource:
    """
    This endpoint takes in:
    1. list of Documents
    2. Use the ImageRef to extract image reference
    3. convert image reference into Object Reference

    """

    def __init__(
        self, documents: List[Document], extractor: Type[ImageRefExtractor]
    ) -> None:
        self.documents = documents
        self.extractor = extractor

    def image_sources(self):
        """for each document, yield a set of ImageSource

        :yield: _description_
        :rtype: _type_
        """
        extra_params = self._get_extractor_extra_keywords()

        for doc in self.documents:
            # search for the extra params in each docs.source keywords
            source_keys = self._retrieve_extra_arguments_from_source(
                doc.source, extra_params
            )

            yield self.extractor(**source_keys).image_sources(doc.content)

    def _get_extractor_extra_keywords(self):
        # extractor allows extra keywords that can be found from the doc.ObjectSource
        params = inspect.signature(self.extractor).parameters.keys()
        return list(params)

    def _retrieve_extra_arguments_from_source(self, source: Source, keys: Sequence):
        try:
            return {key: getattr(source, key) for key in keys}
        except KeyError:
            raise KeyError(
                f"extra keywords {keys} are required by extractor but not found in ObjectSource"
            )
