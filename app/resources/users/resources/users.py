import falcon

from app.media.validators.jsonschema import load_schema, validate
from app.util.error import HTTPError
from ..mappers import UserMapper
from ..models import UserModel


def create_schema():
    return load_schema("./app/resources/users/schemas/create.json")


class Users:
    @validate(create_schema())
    def on_post(self, req, resp):
        db = UserMapper()
        id = str(int(sorted(db.users, key=lambda k: k["id"])[-1]["id"]) + 1)
        um = UserModel(id=id).from_dict(req.media)

        try:
            user = db.create(um)
        except ValueError:
            raise HTTPError(falcon.HTTP_CONFLICT, "Email address already in-use")

        resp.status = falcon.HTTP_CREATED
        resp.media = user.to_dict()

    def on_get(self, req, resp):
        db = UserMapper()
        users = [user.to_dict() for user in db.get_all()]

        resp.media = {"users": users}
