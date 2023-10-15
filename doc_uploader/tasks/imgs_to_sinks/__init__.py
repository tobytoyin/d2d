from typing import List

from doc_uploader.contracts._image_ref_protocols import ImageRefExtractor
from doc_uploader.contracts.document import Document


class ImageFromDocsToSink:
    def __init__(
        self,
        documents: List[Document],
        image_source_extractor: ImageRefExtractor,
        sink,
    ) -> None:
        self._docs = documents
        self._img_extrators = image_source_extractor
        self._sink = sink

    def run(self):
        img_sources = self._get_image_sources()
        return self._sink.dump(img_sources)

    def _get_image_sources(self):
        """for each document, yield a set of ImageSource

        :yield: _description_
        :rtype: _type_
        """
        for doc in self._docs:
            yield self._img_extrators.image_sources(doc.content)
