import os

import pinecone

from d2d.doc_processor.interfaces import Document

API_KEY = os.environ.get("PINECONE_KEY", None)
ENVIRON = os.environ.get("PINECONE_ENV", None)
INDEX = os.environ.get("PINECONE_INDEX", None)

pinecone.init(api_key=API_KEY, environment="gcp-starter")


class PineconeIndexUploader:
    def __init__(self) -> None:
        self.index = pinecone.Index(INDEX)

    def batch_upload(self, iterable, batch_size=100):
        it = iter(iterable)
        chunk = tuple(itertools.islice(it, batch_size))
        while chunk:
            yield chunk
            chunk = tuple(itertools.islice(it, batch_size))
