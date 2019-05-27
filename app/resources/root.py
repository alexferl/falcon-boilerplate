import app.util.json as json


class RootResources:
    def on_get(self, req, resp):
        resp.body = json.dumps({
            "message": "Hello, World!",
        })


class RootNameResources:
    def on_post(self, req, resp, name):
        resp.body = json.dumps({
            "message": "Hello, {}!".format(name.capitalize())
        })
