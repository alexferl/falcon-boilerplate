from .root import RootResources, RootNameResources


def setup_routes(app):
    app.add_route("/", RootResources())
    app.add_route("/{name}", RootNameResources())
