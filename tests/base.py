import unittest

import falcon
import falcon.testing

import app.util.json as json
from app import create_app


class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.srmock = falcon.testing.StartResponseMock()

    def simulate_request(self, path, *args, **kwargs):
        env = falcon.testing.create_environ(path, *args, **kwargs)
        resp = self.app(env, self.srmock)
        if len(resp) >= 1:
            return json.loads(resp[0].decode("utf-8"))
        return resp

    def simulate_get(self, *args, **kwargs):
        kwargs["method"] = "GET"
        return self.simulate_request(*args, **kwargs)

    def simulate_post(self, *args, **kwargs):
        kwargs["method"] = "POST"
        return self.simulate_request(*args, **kwargs)

    def simulate_put(self, *args, **kwargs):
        kwargs["method"] = "PUT"
        return self.simulate_request(*args, **kwargs)

    def simulate_delete(self, *args, **kwargs):
        kwargs["method"] = "DELETE"
        return self.simulate_request(*args, **kwargs)

    def simulate_patch(self, *args, **kwargs):
        kwargs["method"] = "PATCH"
        return self.simulate_request(*args, **kwargs)

    def simulate_head(self, *args, **kwargs):
        kwargs["method"] = "HEAD"
        return self.simulate_request(*args, **kwargs)
