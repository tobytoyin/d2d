# ObsidianMd Image Processor
# extracst the image reference from document
import re
from pathlib import Path
from typing import List, Set

from d2d.contracts.document import Document
from d2d.contracts.source import Source
from d2d.protocols._extract_image_sources import ImageRefExtractor

IMG_PATTERN = r"\!\[\[(.*)\]\](\^.*)?"


class ObsidianRefExtractor(ImageRefExtractor):
    def __init__(self, document: Document, root: Path = Path(".")) -> None:
        self.document = document
        self._root = root

    def image_sources(self) -> Set[Source]:
        labels = self._get_all_labels(self.document.content.contents)

        all_refs = self._get_all_img_refs(self.document.content.contents)
        all_refs = filter(self._filter_file_reference, all_refs)
        all_refs = map(self._cleanup_with_only_image_path, all_refs)
        img_sources = map(self._create_image_source_obj, all_refs, labels)

        return set(img_sources)

    @staticmethod
    def _get_all_img_refs(contents: str) -> List[str]:
        """Get all the ![[.*]] from obsidian md

        :param contents: MD string contents
        :type contents: str
        :return: list of ![[.*]] found from the MD file
        :rtype: List[str]
        """
        file_ref, _ = zip(*re.findall(IMG_PATTERN, contents))
        return file_ref

    @staticmethod
    def _get_all_labels(contents: str) -> List[str]:
        _, labels = zip(*re.findall(IMG_PATTERN, contents))
        labels = [label.replace("^", "") for label in labels]
        return labels

    @staticmethod
    def _filter_file_reference(ref: str) -> bool:
        # filter those ref looks like ![[something#^id]]
        return "#^" not in ref

    @staticmethod
    def _cleanup_with_only_image_path(ref: str) -> str:
        return re.sub(r"\|.*", "", ref)  # remove |scale from file-name|scale

    def _create_image_source_obj(self, ref: str, label: str) -> Source:
        return Source(
            path=self._root.joinpath(Path(ref)),
            source_type=ref.split(".")[-1],
            label=label,  # type: ignore
        )
