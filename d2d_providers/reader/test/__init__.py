from io import StringIO
import pytest


@pytest.fixture
def chunkable_text():
    return io.StringIO("""
                       Hello world
    """)
