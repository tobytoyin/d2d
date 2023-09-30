import os
from functools import cached_property
from typing import Optional

import yaml

PROFILE = os.environ.get("UPLOADER_PROFILE", "profile.yml")


class Profile:
    def __init__(self, path: str = "profile.yml") -> None:
        self.path = path

    @cached_property
    def _profile(self):
        with open(self.path, "r", encoding="utf-8") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc

    def storage(self, _key: Optional[str] = None):
        storage = self._profile.get("storages")

        if not _key:
            return storage

        return storage.get(_key)
