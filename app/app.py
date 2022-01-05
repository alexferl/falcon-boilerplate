import logging
from functools import partial
from typing import Any

import falcon

from app.config import parser, settings
from app.media import json
from app.resources.routes import setup as setup_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

crossorigin_available = True
try:
    from falcon_crossorigin import CrossOrigin
except ImportError:  # pragma: no cover
    crossorigin_available = False

logger = logging.getLogger(__name__)


def configure(**overrides: Any):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser, overrides)
    setup_logging()


def create_app() -> falcon.API:
    mw = []
    if settings.get_bool("CORS_ENABLED"):
        if crossorigin_available is False:
            raise ImportError(
                "'cors-enabled' set but falcon-crossorigin is not installed, "
                "you must install it first to use CORS headers"
            )
        cors = CrossOrigin(
            allow_origins=settings.get("CORS_ALLOW_ORIGINS"),
            allow_methods=settings.get("CORS_ALLOW_METHODS"),
            allow_headers=settings.get("CORS_ALLOW_HEADERS"),
            allow_credentials=settings.get_bool("CORS_ALLOW_CREDENTIALS"),
            expose_headers=settings.get("CORS_EXPOSE_HEADERS"),
            max_age=settings.get_int("CORS_MAX_AGE"),
        )
        mw.append(cors)

    app = falcon.App(middleware=mw)

    dump_kwargs = {"ensure_ascii": False, "sort_keys": True}
    kwargs = json.add_settings_to_kwargs({})
    dump_kwargs.update(kwargs)

    json_handler = falcon.media.JSONHandler(
        dumps=partial(json.dumps, **dump_kwargs),
        loads=partial(json.loads, **kwargs),
    )
    extra_handlers = {
        falcon.MEDIA_JSON: json_handler,
    }

    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)
    app.add_error_handler(Exception, error_handler)

    setup_routes(app)

    return app


def start():
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
