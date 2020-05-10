class HelloName:
    def on_get(self, req, resp, name):
        resp.media = {"message": "Hello, {}!".format(name.capitalize())}
