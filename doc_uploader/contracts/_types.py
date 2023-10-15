from typing import Iterable, Tuple, TypeAlias

from .document import DocUID, Document

IdDocumentPair: TypeAlias = Tuple[DocUID, Document]
DocumentIterable: TypeAlias = Iterable[IdDocumentPair]
