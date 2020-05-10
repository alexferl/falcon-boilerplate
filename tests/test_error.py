import falcon
import pytest

from app.util.error import HTTPError, error_handler


def test_error_handler_raises_on_http_error():
    with pytest.raises(falcon.HTTPError) as excinfo:
        error_handler(None, None, HTTPError, None)

    assert excinfo.value.status == falcon.HTTP_INTERNAL_SERVER_ERROR


def test_error_handler_raises_on_exception():
    with pytest.raises(falcon.HTTPError) as excinfo:
        error_handler(None, None, Exception, None)

    assert excinfo.value.status == falcon.HTTP_INTERNAL_SERVER_ERROR
