import app.util.json as json
from app.util.error import HTTPError


class JSONTranslator:
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise HTTPError(400, "Empty request body. A valid JSON document is required.")

        try:
            req.context.doc = json.loads(body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError):
            raise HTTPError(400,
                            "Malformed JSON. "
                            "Could not decode the request body. The "
                            "JSON was incorrect or not encoded as "
                            "UTF-8.")

    def process_response(self, req, resp, resource, req_succeeded):
        if not hasattr(resp.context, "result"):
            return

        resp.body = json.dumps(resp.context.result)
