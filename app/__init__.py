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

    log_level = kwargs.get('log_level', configs.LOG_LEVEL)
    if log_level:
        setup_logging(configs.LOG_LEVEL)
        logger = logging.getLogger(configs.APP_NAME)
        logger.info('Starting {} in {} mode'.format(configs.APP_NAME,
                                                    configs.ENV))

    app = falcon.API(
        middleware=[
            Crossdomain(),
            JSONTranslator()
        ]
    )

    setup_routes(app)

    return app


def setup_routes(app):
    app.add_route('/', RootResources())
    app.add_route('/{name}', RootNameResources())
