import logging
import os
from typing import Iterable

from .. import TaskCatalog


def test_embedding():
    text = "hello world"
    api_key = os.environ.get("OPENAI_KEY")
    emb = TaskCatalog.embedding(text, api_key=api_key)

    assert "embedding" in emb.keys()
    assert isinstance(emb["embedding"], Iterable)
    logging.info(emb["embedding"][0:10])
