import falcon

from app.media.validators.jsonschema import load_schema, validate
from app.resources import Resource
from app.util.error import HTTPError
from ..mappers import UserMapper
from ..models import UserModel


def schema():
    user = load_schema("../schemas/user.json")
    create = load_schema("../schemas/create.json")
    user = user.update(create)
    return user


class Users(Resource):
    @validate(schema())
    def on_post(self, req, resp):
        mapper = UserMapper(self._db)
        user = UserModel(**req.media)

        try:
            user = mapper.create(user)
        except ValueError:
            raise HTTPError(falcon.HTTP_CONFLICT, "Email address already in-use")

        resp.status = falcon.HTTP_CREATED
        resp.media = user.to_dict()

    def on_get(self, req, resp):
        mapper = UserMapper(self._db)
        users = [user.to_dict() for user in mapper.get_all()]

        resp.media = {"users": users}
