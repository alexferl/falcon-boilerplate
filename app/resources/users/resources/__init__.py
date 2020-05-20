import falcon

from app.data.db import setup

from .user import User, UserSchema
from .users import Users


def get_routes(app: falcon.API):
    db = setup()

    app.add_route("/users", Users(db))
    app.add_route("/users/{user_id}", User(db))
    app.add_route("/user.schema.json", UserSchema())
