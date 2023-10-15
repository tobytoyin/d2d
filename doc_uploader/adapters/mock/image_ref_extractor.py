# ObsidianMd Image Processor
# extracst the image reference from document
import re
from pathlib import Path
from typing import List, Set

from doc_uploader.contracts._image_ref_protocols import ImageRefExtractor
from doc_uploader.contracts.document import DocumentContent
from doc_uploader.contracts.source import ImageSource

IMG_PATTERN = r"\!\[\[(.*)\]\](\^.*)?"


class MockRefExtractor(ImageRefExtractor[DocumentContent]):
    def __init__(self, root: Path = Path(".")) -> None:
        super().__init__()
        self._root = root

    def image_sources(self, content: DocumentContent) -> Set[ImageSource]:
        all_refs = ["img1.png", "img2.png", "img3.png"]
        img_sources = map(self._create_image_source_obj, all_refs)

        return set(img_sources)

    def _create_image_source_obj(self, ref: str) -> ImageSource:
        return ImageSource(
            path=self._root.joinpath(Path(ref)),
            source_type=ref.split(".")[-1],
        )
