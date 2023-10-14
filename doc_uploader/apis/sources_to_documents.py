import itertools
from typing import Iterable, List, Tuple, TypeAlias

from doc_uploader.contracts.document import Document
from doc_uploader.contracts.source import ObjectSource
from doc_uploader.processors import create_document

IdDocumentPair: TypeAlias = Tuple[str, Document]
DocumentIterable: TypeAlias = Iterable[IdDocumentPair]


# Take all the Documents at the beginning and convert them into iterator
class SourcesToDocuments:
    """This endpoint takes in a list of Source Objects and convert them into\
       their variant of iterable of Document objects
    """

    def __init__(self, sources: List[ObjectSource]) -> None:
        self.sources = sources

    def docs_iter(self) -> DocumentIterable:
        for source in self.sources:
            doc = create_document(source=source)
            yield (doc.uid, doc)  # type: ignore

    def docs_batch(self, batch_size=100) -> Iterable[DocumentIterable]:
        docs_iter = iter(self.docs_iter())
        chunk = tuple(itertools.islice(docs_iter, batch_size))
        while chunk:
            yield chunk
            chunk = tuple(itertools.islice(docs_iter, batch_size))
