import logging

import falcon

from app.config import parser, settings
from app.middleware import CrossDomain, JSONTranslator
from app.resources.root import RootResources, RootNameResources
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

logger = logging.getLogger(__name__)


def configure(args):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(args)


def create_app():
    setup_logging()

    app = falcon.API(
        middleware=[
            CrossDomain(),
            JSONTranslator()
        ],
    )

    app.add_error_handler(Exception, error_handler)

    _setup_routes(app)

    return app


def start():
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))


def _setup_routes(app):
    app.add_route("/", RootResources())
    app.add_route("/{name}", RootNameResources())
