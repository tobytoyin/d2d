from io import IOBase
from typing import Callable, Protocol

from .source import Source


class SourceTasks(Protocol):
    def source_io(self, d: dict) -> IOBase:
        ...

    def summary_task(self, d: dict) -> dict:
        ...
