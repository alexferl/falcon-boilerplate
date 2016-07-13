import logging

import falcon

from app.config import DevConfig, ProdConfig, configs
from app.middleware import Crossdomain, JSONTranslator
from app.resources.root import RootResources, RootNameResources
from app.util.logs import setup_logging


def create_app(env, **kwargs):
    if env == 'DEV':
        configs = DevConfig
    elif env == 'PROD':
        configs = ProdConfig
    else:
        configs = DevConfig

    app = falcon.API(
        middleware=[
            Crossdomain(),
            JSONTranslator()
        ]
    )

    setup_logging(configs.LOG_LEVEL)
    logger = logging.getLogger(configs.APP_NAME)
    setup_routes(app)

    logger.info('Starting app in {} mode'.format(configs.ENV))

    return app


def setup_routes(app):
    app.add_route('/', RootResources())
    app.add_route('/{name}', RootNameResources())

    return app
