import falcon
import pytest
from mock import patch

from app.resources.users.mappers import UserMapper
from .. import user1, user2
from . import skip_missing_dep


@skip_missing_dep
def test_create_user(client):
    doc = {
        "first_name": "Test3",
        "last_name": "User3",
        "email": "testuser3@example.com",
    }

    result = client.simulate_post("/users", json=doc)

    assert result.status == falcon.HTTP_CREATED
    assert result.json["first_name"] == doc["first_name"]
    assert result.json["last_name"] == doc["last_name"]
    assert result.json["email"] == doc["email"]


@skip_missing_dep
@pytest.mark.parametrize("user", (user1(),))
def test_create_user_already_exists(client, user):
    doc = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }
    with patch.object(UserMapper, "_find_by_email_or_id", return_value=user):
        result = client.simulate_post("/users", json=doc)
        assert result.status == falcon.HTTP_CONFLICT


def test_get_users(client):
    with patch.object(UserMapper, "get_all", return_value=[user1(), user2()]):
        result = client.simulate_get("/users")

        assert result.status == falcon.HTTP_OK
        assert len(result.json["users"]) == 2
