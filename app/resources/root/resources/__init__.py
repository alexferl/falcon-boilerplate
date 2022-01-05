import falcon

from .hello import HelloName
from .root import Root


def get_routes(app: falcon.App):
    app.add_route("/", Root())
    app.add_route("/hello/{name}", HelloName())
