from datetime import datetime
from uuid import UUID

import pytest

from app.data.db import setup
from app.resources.users.mappers import UserMapper
from app.resources.users.models import UserModel
from .. import user1, user2


@pytest.fixture
def mapper():
    db = setup()
    mapper = UserMapper(db)
    mapper._db._data = []
    return mapper


def test_create(mapper):
    new_user = UserModel(
        id=UUID("6b5a3e0e-ca4d-44f8-93cd-26f57ea3f705"),
        first_name="New",
        last_name="User",
        email="newuser@example.com",
    )
    result = mapper.create(new_user)

    assert result.id == new_user.id
    assert result.first_name == new_user.first_name
    assert result.last_name == new_user.last_name
    assert result.email == new_user.email
    assert result.created_at == new_user.created_at


def test_create_exists(mapper):
    mapper._db._data = [user1().to_dict()]
    with pytest.raises(ValueError):
        mapper.create(user1())


def test_get(mapper):
    user = user1()
    mapper._db._data = [user1().to_dict()]
    result = mapper.get("1f0d047364014d18864f492989276641")

    assert result.id == user.id
    assert result.first_name == user.first_name
    assert result.last_name == user.last_name
    assert result.email == user.email
    assert result.created_at == user.created_at


def test_get_with_uuid(mapper):
    user = user1()
    mapper._db._data = [user1().to_dict()]
    result = mapper.get(UUID("1f0d0473-6401-4d18-864f-492989276641"))

    assert result.id == user.id


def test_get_all(mapper):
    mapper._db._data = [user1().to_dict(), user2().to_dict()]
    result = mapper.get_all()

    assert len(result) == 2


def test_get_all_deleted(mapper):
    user = user2()
    user.deleted_at = datetime.now()
    mapper._db._data = [user1().to_dict(), user.to_dict()]
    result = mapper.get_all()

    assert len(result) == 1


def test_get_all_empty(mapper):
    result = mapper.get_all()

    assert result == []


def test_update(mapper):
    user = user1()
    mapper._db._data = [user.to_dict()]
    doc = {"last_name": "Updated"}
    user = user.update(doc)
    mapper.save(user)

    assert user.last_name == doc["last_name"]
    assert user.updated_at is not None


def test_delete(mapper):
    user = user1()
    mapper._db._data = [user.to_dict()]
    user.delete()
    mapper.save(user)

    assert user.deleted_at is not None


def test_find_by_email(mapper):
    user = user1()
    mapper._db._data = [user.to_dict()]
    result = mapper.find_by_email(user.email)

    assert result.email == user.email
