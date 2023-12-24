import logging
import os
from typing import Iterable

from .. import TaskCatalog


def test_embedding():
    text = "hello world"
    api_key = os.environ.get("OPENAI_KEY")
    emb = TaskCatalog.embedding(text, api_key=api_key)

    assert "vector" in emb.keys()
    assert isinstance(emb["vector"], Iterable)
    logging.info(emb["vector"][0:10])
