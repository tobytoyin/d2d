# ObsidianMd Image Processor
# extracst the image reference from document
import re
from pathlib import Path
from typing import List, Set

from doc_uploader.contracts._image_ref_protocols import ImageRefExtractor
from doc_uploader.contracts.document import DocumentContent
from doc_uploader.contracts.source import ImageSource

IMG_PATTERN = r"\!\[\[(.*)\]\](\^.*)?"


class ObsidianRefExtractor(ImageRefExtractor[DocumentContent]):
    def __init__(self, root: Path = Path(".")) -> None:
        super().__init__()
        self._root = root

    def image_sources(self, content: DocumentContent) -> Set[ImageSource]:
        all_refs = self._get_all_img_refs(content.contents)
        all_refs = filter(self._filter_file_reference, all_refs)
        all_refs = map(self._cleanup_with_only_image_path, all_refs)

        img_sources = map(self._create_image_source_obj, all_refs)

        return set(img_sources)

    def _get_all_img_refs(self, contents: str) -> List[str]:
        """Get all the ![[.*]] from obsidian md

        :param contents: MD string contents
        :type contents: str
        :return: list of ![[.*]] found from the MD file
        :rtype: List[str]
        """
        file_ref, _ = zip(*re.findall(IMG_PATTERN, contents))
        return file_ref

    def _get_all_id_refs(self, contents: str) -> List[str]:
        _, id_ref = zip(*re.findall(IMG_PATTERN, contents))
        return id_ref

    def _filter_file_reference(self, ref: str) -> bool:
        # filter those ref looks like ![[something#^id]]
        return "#^" not in ref

    def _cleanup_with_only_image_path(self, ref: str) -> str:
        return re.sub(r"\|.*", "", ref)  # remove |scale from file-name|scale

    def _create_image_source_obj(self, ref: str) -> ImageSource:
        return ImageSource(
            path=self._root.joinpath(Path(ref)),
            source_type=ref.split(".")[-1],
        )
