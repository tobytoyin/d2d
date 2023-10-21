from typing import Protocol

from d2d.contracts._types import DocumentIterable


class DocumentService(Protocol):
    """DocumentService shares the same interface that accept the following:
    - `documents_iter` - an Iterable of (DocUID, Document), this can be \
        uniformly generated via `source_handlers.sources_to_documents`

    :param Protocol: _description_
    :type Protocol: _type_
    """

    documents: DocumentIterable
