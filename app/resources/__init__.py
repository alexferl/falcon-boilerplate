from .root import Root, RootName


def setup_routes(app):
    app.add_route("/", Root())
    app.add_route("/{name}", RootName())
