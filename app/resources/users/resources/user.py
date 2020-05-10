import falcon

from app.data.mapper import resolve_obj
from app.media.validators.jsonschema import load_schema, validate
from ..mappers import UserMapper


def update_schema():
    return load_schema("./app/resources/users/schemas/update.json")


class User:
    def on_get(self, req, resp, user_id):
        user = resolve_obj(user_id, UserMapper())

        resp.media = user.to_dict()

    @validate(update_schema())
    def on_put(self, req, resp, user_id):
        db = UserMapper()
        user = resolve_obj(user_id, db)

        user.update(req.media)
        db.save(user)

        resp.media = user.to_dict()

    def on_delete(self, req, resp, user_id):
        db = UserMapper()
        user = resolve_obj(user_id, db)

        user.delete()
        db.save(user)

        resp.status = falcon.HTTP_NO_CONTENT
