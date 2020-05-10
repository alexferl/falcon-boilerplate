class Root:
    def on_get(self, req, resp):
        resp.media = {"message": "Hello, World!"}
