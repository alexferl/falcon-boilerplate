import falcon

from .root import get_routes as root_routes
from .users import get_routes as users_routes


def setup_routes(app: falcon.API):
    for routes in (root_routes, users_routes):
        routes(app)
