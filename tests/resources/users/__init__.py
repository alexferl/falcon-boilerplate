from app.resources.users.models import UserModel


def user1():
    return UserModel(
        id="1",
        first_name="Test1",
        last_name="User1",
        email="testuser1@example.com",
        created_at="2020-05-09T16:20:00.000000Z",
    )


def user2():
    return UserModel(
        id="2",
        first_name="Test2",
        last_name="User2",
        email="testuser2@example.com",
        created_at="2020-05-09T16:21:00.000000Z",
    )
