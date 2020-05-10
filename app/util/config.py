import argparse
import os
from typing import Any, Dict

from vyper import v

settings = v


def setup_vyper(parser: argparse.ArgumentParser, overrides: Dict[str, Any] = None):
    env_name = os.getenv("APP_ENV_NAME", "LOCAL").lower()
    config_name = "config.{}".format(env_name)

    v.bind_args(parser)

    if overrides:  # pragma: no cover
        for k, val in overrides.items():
            v.set(k, val)

    v.set_env_prefix(v.get("environment_variables_prefix"))
    v.set_env_key_replacer("-", "_")
    v.automatic_env()

    v.add_config_path("config")
    v.set_config_type("toml")
    v.set_config_name(config_name)
    v.read_in_config()
