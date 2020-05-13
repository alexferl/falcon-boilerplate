import logging

import falcon

logger = logging.getLogger(__name__)


class HTTPError(falcon.HTTPError):
    def __init__(self, status: str, description: str, **kwargs: dict):
        super().__init__(status, status, str(description), **kwargs)


def error_handler(req, resp, ex, params):
    if not isinstance(ex, falcon.HTTPError):
        logger.exception("Unhandled error while processing request: {}".format(ex))
        raise HTTPError(falcon.HTTP_INTERNAL_SERVER_ERROR, str(ex))
    else:
        raise ex
