from typing import Literal, TypeAlias

TaskKeyword: TypeAlias = Literal[
    "summary",
    "metadata",
    "relations",
    "embedding",
    "content",
    "obj_refs",
    "named_entity_relations",
]
