from datetime import datetime

from xid import XID

from app.resources.users.models import UserModel


def user1():
    return UserModel(
        id=XID("bsqpe67f38q71u3sq6og"),
        first_name="Test1",
        last_name="User1",
        email="testuser1@example.com",
        created_at=datetime(2020, 5, 9, 16, 20, 00, 000000),
    )


def user2():
    return UserModel(
        id=XID("bsqpea7f38q71u3sq6p0"),
        first_name="Test2",
        last_name="User2",
        email="testuser2@example.com",
        created_at=datetime(2020, 5, 9, 16, 21, 00, 000000),
    )
