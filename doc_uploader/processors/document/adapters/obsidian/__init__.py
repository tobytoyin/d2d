from functools import cached_property

from doc_uploader.contracts._source import DocumentSource


class ObsidianMd(DocumentSource):
    @cached_property
    def text(self):
        with open(self.source, "r") as f:
            return f.read()

    @property
    def contents(self) -> str:
        return self.text

    @property
    def bytes(self) -> bytes:
        return self.text.encode()
