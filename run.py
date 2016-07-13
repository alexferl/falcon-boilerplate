from app import create_app


def init_app(env='DEV', **kwargs):
    return create_app(env.upper(), **kwargs)
