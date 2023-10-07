import itertools
from typing import Iterable, List, Tuple, TypeAlias

from pydantic import BaseModel

from doc_uploader.doc_processor.factory import create_document
from doc_uploader.doc_processor.interfaces import Document
from doc_uploader.doc_processor.types import DocID

IdDocumentPair: TypeAlias = Tuple[DocID, Document]
DocumentIterable: TypeAlias = Iterable[IdDocumentPair]


class DocumentParserInput(BaseModel):
    source: str
    files: List[str]


# Take all the Documents at the beginning and convert them into iterator
class DocumentsParser:
    """Parse and processor the documents from the source and return iterables"""

    def __init__(self, payload: DocumentParserInput) -> None:
        self.payload = payload

    def docs_iter(self) -> DocumentIterable:
        for f in self.payload.files:
            doc = create_document(self.payload.source, f)
            yield (doc.uid, doc)

    def docs_batch(self, batch_size=100) -> Iterable[DocumentIterable]:
        docs_iter = iter(self.docs_iter())
        chunk = tuple(itertools.islice(docs_iter, batch_size))
        while chunk:
            yield chunk
            chunk = tuple(itertools.islice(docs_iter, batch_size))
