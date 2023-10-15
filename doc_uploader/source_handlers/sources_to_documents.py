import itertools
from typing import Iterable, List, Tuple, TypeAlias

from doc_uploader.adapters.factory import create_document
from doc_uploader.contracts._types import DocumentIterable
from doc_uploader.contracts.source import Source


def sources_to_documents(sources: List[Source]) -> DocumentIterable:
    """Takes in a list of SourceObjects and convert them into documents Iterable

    :param sources: list of source objects
    :type sources: List[ObjectSource]
    :yield: tuple of document.uid and the document itself
    :rtype: Generator(DocUID, Document)
    """
    for source in sources:
        doc = create_document(source=source)
        yield (doc.uid, doc)  # type: ignore


def sources_to_documents_batches(
    sources: List[Source],
    batch_size: int = 100,
) -> Iterable[DocumentIterable]:
    """Takes in a list of SourceObjects and convert them into documents Batches

    :param sources: _description_
    :type sources: List[ObjectSource]
    :param batch_size: _description_, defaults to 100
    :type batch_size: int, optional
    :return: _description_
    :rtype: Iterable[DocumentIterable]
    :yield: _description_
    :rtype: Iterator[Iterable[DocumentIterable]]
    """
    docs_iter = iter(sources_to_documents(sources))
    chunk = tuple(itertools.islice(docs_iter, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(docs_iter, batch_size))
