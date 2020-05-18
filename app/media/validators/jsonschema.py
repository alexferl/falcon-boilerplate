# code based on falcon.media.validators.jsonschema

import inspect
from functools import wraps
from pathlib import Path

import falcon
from falcon.media.validators.jsonschema import validate as falcon_validate

from app.media import json
from app.util.error import HTTPError

fastjsonschema_available = True
try:
    import fastjsonschema
except ImportError:  # pragma: no cover
    fastjsonschema_available = False


def load_schema(rel_path: str) -> dict:
    """
    Loads a schema from a relative path of the caller of this function.
    :param rel_path: Relative path from the caller. e.g. ../schemas/schema.json
    :return: Loaded schema as a `dict`.
    """
    caller_path = Path((inspect.stack()[1])[1]).parent
    fp = (caller_path / rel_path).resolve()

    with open(fp, "r") as fh:
        data = json.loads(fh.read())
        return data


def _validate(req_schema: dict = None, resp_schema: dict = None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, req, resp, *args, **kwargs):
            if req_schema is not None:
                try:
                    schema = fastjsonschema.compile(req_schema)
                    schema(req.media)
                except fastjsonschema.JsonSchemaException as e:
                    msg = "Request data failed validation: {}".format(e.message)
                    raise HTTPError(falcon.HTTP_BAD_REQUEST, msg)

            result = func(self, req, resp, *args, **kwargs)

            if resp_schema is not None:
                try:
                    schema = fastjsonschema.compile(resp_schema)
                    schema(resp.media)
                except fastjsonschema.JsonSchemaException:
                    raise HTTPError(
                        falcon.HTTP_INTERNAL_SERVER_ERROR,
                        "Response data failed validation",
                    )
                    # Do not return 'e.message' in the response to
                    # prevent info about possible internal response
                    # formatting bugs from leaking out to users.

            return result

        return wrapper

    return decorator


if fastjsonschema_available is False:
    validate = falcon_validate  # pragma: no cover
else:
    validate = _validate
