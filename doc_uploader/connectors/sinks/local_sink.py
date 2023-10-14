from doc_uploader.contracts.source import ImageSource


class LocalSink:
    def __init__(self, sources: ImageSource) -> None:
        self.sources = sources

    def dump(self):
        return list(self.sources)
