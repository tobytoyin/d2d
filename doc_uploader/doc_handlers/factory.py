from .obsidian.adapter import ObsidianDocument

# class DocHandlerFactory:
#     @staticmethod
#     def obsidian(path: str):
#         return ObsidianDocument(path=path)


@property
def document(self) -> BaseDocument:
    return BaseDocument(
        uid=self.id,
        contents=self.contents,
        metadata=self.metadata,
        relations=self.relations,
    )


def document_factory():
    ...
