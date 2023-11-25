from typing import Protocol, TypeVar

T = TypeVar("T")


class DocumentToDB(Protocol[T]):
    def update_or_create_document(self, _: T, /, *args, **kwargs):
        ...

    def delete_document(self, _: T, /, *args, **kwargs):
        ...
