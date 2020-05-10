import falcon

from .user import User
from .users import Users


def get_routes(app: falcon.API):
    app.add_route("/users", Users())
    app.add_route("/users/{user_id}", User())
