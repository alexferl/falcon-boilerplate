import falcon

import app.util.serialization as json


class Crossdomain(object):
    def process_response(self, req, resp, resource):
        resp.set_header('Access-Control-Allow-Origin', '*')  # Change in prod
        resp.set_header('Access-Control-Allow-Methods',
                        'GET, PUT, POST, DELETE')
        resp.set_header('Access-Control-Allow-Credentials', 'true')
        resp.set_header(
            'Access-Control-Allow-Headers',
            'Origin, Authorization, Content-Type, X-Requested-With')


class JSONTranslator(object):
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPBadRequest(
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect or not encoded as '
                'UTF-8.')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps(req.context['result'])
