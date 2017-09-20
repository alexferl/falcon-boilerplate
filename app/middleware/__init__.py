import app.util.json as json
from app.config import settings
from app.util.error import HTTPError


class CrossDomain(object):
    def process_response(self, req, resp, resource):
        resp.set_header("Access-Control-Allow-Origin",
                        settings.get("ACCESS_CONTROL_ALLOW_ORIGIN"))
        resp.set_header("Access-Control-Allow-Methods",
                        settings.get("ACCESS_CONTROL_ALLOW_METHODS"))
        resp.set_header("Access-Control-Allow-Credentials",
                        settings.get("ACCESS_CONTROL_ALLOW_CREDENTIALS"))
        resp.set_header("Access-Control-Allow-Headers",
                        settings.get("ACCESS_CONTROL_ALLOW_HEADERS"))


class JSONTranslator(object):
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise HTTPError(400, "A valid JSON document is required.")

        try:
            req.context["doc"] = json.loads(body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError):
            raise HTTPError(400, "Could not decode the request body. The "
                                 "JSON was incorrect or not encoded as "
                                 "UTF-8.")

    def process_response(self, req, resp, resource):
        if "result" not in req.context:
            return

        resp.body = json.dumps(req.context["result"])
