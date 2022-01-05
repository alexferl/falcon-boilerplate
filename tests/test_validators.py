try:
    import fastjsonschema
except ImportError:
    fastjsonschema = None

import falcon
import pytest
from falcon import testing

from app.media import validators
from app.util.error import HTTPError

basic_schema = {
    "type": "object",
    "properties": {"message": {"type": "string"}},
    "required": ["message"],
}


skip_missing_dep = pytest.mark.skipif(
    fastjsonschema is None, reason="fastjsonschema dependency not found"
)


class Resource:
    @validators.jsonschema._validate(req_schema=basic_schema)
    def request_validated(self, req, resp):
        assert req.media is not None
        return resp

    @validators.jsonschema._validate(resp_schema=basic_schema)
    def response_validated(self, req, resp):
        assert resp.media is not None
        return resp

    @validators.jsonschema._validate(req_schema=basic_schema, resp_schema=basic_schema)
    def both_validated(self, req, resp):
        assert req.media is not None
        assert resp.media is not None
        return req, resp

    @validators.jsonschema._validate(req_schema=basic_schema, resp_schema=basic_schema)
    def on_put(self, req, resp):
        assert req.media is not None
        resp.media = GoodData.media


class GoodData:
    media = {"message": "something"}


class BadData:
    media = {}


@skip_missing_dep
def test_req_schema_validation_success():
    data = GoodData()
    assert Resource().request_validated(GoodData(), data) is data


@skip_missing_dep
def test_req_schema_validation_failure():
    with pytest.raises(falcon.HTTPError) as excinfo:
        Resource().request_validated(BadData(), None)

    msg = "Request data failed validation: data must contain ['message'] properties"
    assert excinfo.value.title == falcon.HTTP_BAD_REQUEST
    assert excinfo.value.description == msg


@skip_missing_dep
def test_resp_schema_validation_success():
    data = GoodData()
    assert Resource().response_validated(GoodData(), data) is data


@skip_missing_dep
def test_resp_schema_validation_failure():
    with pytest.raises(HTTPError) as excinfo:
        Resource().response_validated(GoodData(), BadData())

    assert excinfo.value.title == falcon.HTTP_INTERNAL_SERVER_ERROR
    assert excinfo.value.description == "Response data failed validation"


@skip_missing_dep
def test_both_schemas_validation_success():
    req_data = GoodData()
    resp_data = GoodData()

    result = Resource().both_validated(req_data, resp_data)

    assert result[0] is req_data
    assert result[1] is resp_data

    client = testing.TestClient(falcon.App())
    client.app.add_route("/test", Resource())
    result = client.simulate_put("/test", json=GoodData.media)
    assert result.json == resp_data.media


@skip_missing_dep
def test_both_schemas_validation_failure():
    with pytest.raises(HTTPError) as excinfo:
        Resource().both_validated(GoodData(), BadData())

    assert excinfo.value.title == falcon.HTTP_INTERNAL_SERVER_ERROR
    assert excinfo.value.description == "Response data failed validation"

    with pytest.raises(HTTPError) as excinfo:
        Resource().both_validated(BadData(), GoodData())

    msg = "Request data failed validation: data must contain ['message'] properties"
    assert excinfo.value.title == falcon.HTTP_BAD_REQUEST
    assert excinfo.value.description == msg

    client = testing.TestClient(falcon.App())
    client.app.add_route("/test", Resource())
    result = client.simulate_put("/test", json=BadData.media)
    assert result.status_code == 400
