import app.util.json as json


class RootResources(object):
    def on_get(self, req, resp):
        resp.body = json.dumps({
            "message": "Hello, World!",
        })


class RootNameResources(object):
    def on_post(self, req, resp, name):
        resp.body = json.dumps({
            "message": "Hello, {}!".format(name.capitalize())
        })
