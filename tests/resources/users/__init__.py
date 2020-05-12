from datetime import datetime
from uuid import UUID

from app.resources.users.models import UserModel


def user1():
    return UserModel(
        id=UUID("1f0d0473-6401-4d18-864f-492989276641"),
        first_name="Test1",
        last_name="User1",
        email="testuser1@example.com",
        created_at=datetime(2020, 5, 9, 16, 20, 00, 000000),
    )


def user2():
    return UserModel(
        id=UUID("4371b50a-dd54-4849-959f-ad2321ade57c"),
        first_name="Test2",
        last_name="User2",
        email="testuser2@example.com",
        created_at=datetime(2020, 5, 9, 16, 21, 00, 000000),
    )
