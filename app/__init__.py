import logging
from functools import partial

import falcon

try:
    from falcon_crossorigin import CrossOrigin
except ImportError:  # pragma: no cover
    pass

from app.config import parser, settings
from app.media import json
from app.resources import setup_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging

logger = logging.getLogger(__name__)


def configure(**overrides: str):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser, overrides)
    setup_logging()


def create_app() -> falcon.API:
    mw = []
    if settings.get_bool("CORS_ENABLED"):  # pragma: no cover
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

    dump_kwargs = {"ensure_ascii": False, "sort_keys": True}
    kwargs = json.add_settings_to_kwargs({})
    dump_kwargs.update(kwargs)

    json_handler = falcon.media.JSONHandler(
        dumps=partial(json.dumps, **dump_kwargs), loads=partial(json.loads, **kwargs),
    )
    extra_handlers = {
        falcon.MEDIA_JSON: json_handler,
    }

    app.req_options.media_handlers.update(extra_handlers)
    app.resp_options.media_handlers.update(extra_handlers)
    app.add_error_handler(Exception, error_handler)

    setup_routes(app)

    return app


def start():  # pragma: no cover
    logger.info("Starting {}".format(settings.get("APP_NAME")))
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
