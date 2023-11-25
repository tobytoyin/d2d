import importlib
import os
import tomllib

CONFIG_PATH = os.environ.get("CONFIG_PATH", "configs/config.toml")


class Config:
    @staticmethod
    def get_providers() -> dict:
        with open(CONFIG_PATH, "rb") as f:
            config = tomllib.load(f).get("providers")

        if not config:
            raise FileNotFoundError(
                f"{CONFIG_PATH} does not exist. Set $CONFIG_PATH if its in a different location",
            )
        return config
