from .obsidian.model import ObsidianDocument


class DocHandlerFactory:
    @staticmethod
    def obsidian(path: str):
        return ObsidianDocument(path=path)
