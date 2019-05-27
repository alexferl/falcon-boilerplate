import logging
from functools import partial

import falcon
import rapidjson
from falcon import media

from app.config import parser, settings
from app.middleware import CrossDomain, JSONTranslator
from app.resources import setup_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

logger = logging.getLogger(__name__)


def configure():
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser)
    setup_logging()


def create_app():
    app = falcon.API(
        middleware=[
            CrossDomain(),
            JSONTranslator()
        ]
    )

    json_handler = media.JSONHandler(
        dumps=partial(
            rapidjson.dumps,
            ensure_ascii=False, sort_keys=True
        ),
        loads=rapidjson.loads
    )
    extra_handlers = {
        'application/json': json_handler,
    }

    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)
    app.add_error_handler(Exception, error_handler)

    setup_routes(app)

    return app


def start():
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
