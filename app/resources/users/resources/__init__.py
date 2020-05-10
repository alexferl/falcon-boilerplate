import falcon

from .user import User, UserSchema
from .users import Users


def get_routes(app: falcon.API):
    app.add_route("/users", Users())
    app.add_route("/users/{user_id}", User())
    app.add_route("/user.schema.json", UserSchema())
