import logging

import falcon

from app.config import parser, settings
from app.middleware import CrossDomain, JSONTranslator
from app.resources import setup_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

logger = logging.getLogger(__name__)


def configure(args=None):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(args)
    setup_logging()


def create_app():
    app = falcon.API(
        middleware=[
            CrossDomain(),
            JSONTranslator()
        ]
    )

    app.add_error_handler(Exception, error_handler)

    setup_routes(app)

    return app


def start():
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
