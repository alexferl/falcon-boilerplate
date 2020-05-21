import falcon

from app.data import retrieve_obj
from app.media.validators.jsonschema import load_schema, validate
from app.resources import Resource
from ..mappers import UserMapper


def schema():
    return load_schema("../schemas/user.json")


class User(Resource):
    def on_get(self, req, resp, user_id):
        user = retrieve_obj(user_id, UserMapper(self._db))

        resp.media = user.to_dict()

    @validate(schema())
    def on_put(self, req, resp, user_id):
        mapper = UserMapper(self._db)
        user = retrieve_obj(user_id, mapper)

        user = user.update(req.media)
        mapper.save(user)

        resp.media = user.to_dict()

    def on_delete(self, req, resp, user_id):
        mapper = UserMapper(self._db)
        user = retrieve_obj(user_id, mapper)

        user.delete()
        mapper.save(user)

        resp.status = falcon.HTTP_NO_CONTENT


class UserSchema:
    def on_get(self, req, resp):
        resp.media = schema()
