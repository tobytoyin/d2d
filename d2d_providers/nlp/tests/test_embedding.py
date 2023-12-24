import logging
import os
from typing import Iterable

from .. import TaskCatalog


def test_embedding():
    text = "hello world\rgood bye world"
    emb = TaskCatalog.embedding(text)

    logging.info(emb["vector"][0:10])

    assert "vector" in emb.keys()
    assert isinstance(emb["vector"], Iterable)
