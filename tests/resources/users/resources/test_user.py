import falcon
import pytest
from mock import patch

from app.resources.users.mappers import UserMapper
from .. import user1
from . import skip_missing_dep


@skip_missing_dep
@pytest.mark.parametrize("user", (user1(),))
def test_get_user(client, user):
    with patch.object(UserMapper, "get", return_value=user):
        result = client.simulate_get("/users/{}".format(user.id))

        assert result.status == falcon.HTTP_OK
        assert result.json["id"] == str(user.id)
        assert result.json["first_name"] == user.first_name
        assert result.json["last_name"] == user.last_name
        assert result.json["email"] == user.email


@skip_missing_dep
@pytest.mark.parametrize("user", (user1(),))
def test_delete_user(client, user):
    with patch.object(UserMapper, "get", return_value=user):
        result = client.simulate_delete("/users/{}".format(user.id))

        assert result.status == falcon.HTTP_NO_CONTENT

        result = client.simulate_delete("/users/{}".format(user.id))

        assert result.status == falcon.HTTP_GONE
        assert user.deleted_at is not None


@skip_missing_dep
@pytest.mark.parametrize("user", (user1(),))
def test_edit_user(client, user):
    doc = {"last_name": "changed"}
    with patch.object(UserMapper, "get", return_value=user):
        result = client.simulate_put("/users/".format(user.id), json=doc)

        assert result.status == falcon.HTTP_OK
        assert result.json["last_name"] == doc["last_name"]
        assert result.json["updated_at"] is not None


def test_get_schema(client):
    result = client.simulate_get("/user.schema.json")

    assert result.status == falcon.HTTP_OK
    assert result.json["description"] == "A user account."
