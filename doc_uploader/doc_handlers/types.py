from typing import Dict, List, Literal, TypeAlias, Union

VT: TypeAlias = List | str | int
KT: TypeAlias = str
DocTypeVT: TypeAlias = str
DocTypeKT: TypeAlias = Literal["doc_type"]
MetadataKVPair: TypeAlias = Union[Dict[KT, VT], Dict[DocTypeKT, DocTypeKT]]

DocID: TypeAlias = str
NormalisedContents: TypeAlias = str
