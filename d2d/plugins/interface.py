from typing import Protocol, TypeVar

from d2d.contracts.documents import Document

T = TypeVar("T")


class DocumentPlugin:
    def update_or_create_document(self, _: Document, /, **kwargs):
        ...

    def delete_document(self, _: Document, /, **kwargs):
        ...

    # object storage capabilities
    def put_objects(self, _: Document, /, **kwargs):
        ...
