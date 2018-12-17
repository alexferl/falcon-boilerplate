import os

from vyper import v

settings = v


def setup_vyper(parser):
    env_name = os.getenv("APP_ENV_NAME", "LOCAL").lower()
    config_name = "config.{}".format(env_name)

    v.bind_args(parser)

    v.set_env_prefix(v.get("environment_variables_prefix"))
    v.set_env_key_replacer("-", "_")
    v.automatic_env()

    v.add_config_path("config")
    v.set_config_type("toml")
    v.set_config_name(config_name)
    v.read_in_config()
