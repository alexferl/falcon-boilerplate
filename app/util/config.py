import os

from vyper import v

settings = v


def _get_default_args(args):
    return {k: args.get_default(k) for k in _get_args(args).keys()}


def _get_args(args):
    return vars(args.parse_args([]))


def _setup_args(args):
    defaults = _get_default_args(args)
    args_dict = _get_args(args)
    for k, val in defaults.items():
        v.set_default(k, val)
        if v.get(k) != args_dict[k]:
            v.bind_arg(k, args_dict[k])


def _setup_overrides(overrides):
    for k, val in overrides.items():
        v.set(k, val)


def setup_vyper(parser, overrides):
    defaults = _get_default_args(parser)

    actual_overrides = \
        {k: val for k, val in overrides.items() if defaults[k] != val}
    env_name = os.getenv("APP_ENV_NAME", "LOCAL").lower()
    config_name = "config.{}".format(env_name)

    _setup_args(parser)
    _setup_overrides(actual_overrides)

    v.set_env_prefix(v.get("environment_variables_prefix"))
    v.set_env_key_replacer("-", "_")
    v.automatic_env()

    v.add_config_path("config")
    v.set_config_type("toml")
    v.set_config_name(config_name)
    v.read_in_config()
