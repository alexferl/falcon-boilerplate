from typing import List, Union

from app.data.mapper import BaseMapper
from ..models import UserModel

USERS = [
    {
        "id": "1",
        "created_at": "2020-05-09T16:20:40.560920Z",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
    },
    {
        "id": "2",
        "created_at": "2020-05-09T16:21:01.326478Z",
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
    },
]


class UserMapper(BaseMapper):
    def __init__(self):
        global USERS
        self.users = USERS

    def _get_index(self, user_id: str):
        for idx, user in enumerate(self.users):
            if user["id"] == user_id:
                return idx

    def find_by_email(self, email: str) -> Union[UserModel, None]:
        for user in self.users:
            if user["email"] == email:
                return UserModel().from_dict(user)

    def create(self, user: UserModel) -> UserModel:
        exists = self.find_by_email(user.email)
        if exists:
            raise ValueError
        self.users.append(user.to_dict())
        return self.get(user.id)

    def get(self, user_id: str) -> Union[UserModel, None]:
        for user in self.users:
            if user["id"] == user_id:
                return UserModel().from_dict(user)

    def get_all(self) -> Union[List[UserModel], None]:
        if len(self.users) < 1:
            return []

        users = []
        for user in self.users:
            o = UserModel().from_dict(user)
            if getattr(o, "deleted_at") and o.deleted_at is not None:
                continue
            else:
                users.append(o)
        return users

    def save(self, user: UserModel) -> UserModel:
        pos = self._get_index(user.id)
        if pos is not None:
            self.users[pos] = user.to_dict()

        return user
