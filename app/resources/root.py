class RootResources:
    def on_get(self, req, resp):
        resp.media = {
            "message": "Hello, World!",
        }


class RootNameResources:
    def on_post(self, req, resp, name):
        resp.media = {
            "message": "Hello, {}!".format(name.capitalize())
        }
