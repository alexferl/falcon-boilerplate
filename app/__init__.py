import logging
from functools import partial

import falcon
import rapidjson
from falcon import media
from falcon_crossorigin import CrossOrigin

from app.config import parser, settings
from app.middleware import JSONTranslator
from app.resources import setup_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

logger = logging.getLogger(__name__)


def configure(**overrides):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser, overrides)
    setup_logging()


def create_app():
    mw = [JSONTranslator()]
    if settings.get_bool("CORS_ENABLED"):
        cors = CrossOrigin(
            allow_origins=settings.get("CORS_ALLOW_ORIGINS"),
            allow_methods=settings.get("CORS_ALLOW_METHODS"),
            allow_headers=settings.get("CORS_ALLOW_HEADERS"),
            allow_credentials=settings.get_bool("CORS_ALLOW_CREDENTIALS"),
            expose_headers=settings.get("CORS_EXPOSE_HEADERS"),
            max_age=settings.get_int("CORS_MAX_AGE"),
        )
        mw.append(cors)

    app = falcon.API(middleware=mw)

    json_handler = media.JSONHandler(
        dumps=partial(rapidjson.dumps, ensure_ascii=False, sort_keys=True),
        loads=rapidjson.loads,
    )
    extra_handlers = {
        "application/json": json_handler,
    }

    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)
    app.add_error_handler(Exception, error_handler)

    setup_routes(app)

    return app


def start():
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
