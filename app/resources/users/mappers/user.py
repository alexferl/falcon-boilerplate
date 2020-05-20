from typing import List, Union
from uuid import UUID

from app.data.mapper import Mapper
from ..models import UserModel


class UserMapper(Mapper):
    def __init__(self, db):
        super().__init__(db)

    def create(self, user: UserModel) -> UserModel:
        exists = self._find_by_email_or_id(user.email, user.id)
        if exists:
            raise ValueError

        self._db.insert(user.to_dict())

        return self.get(user.id)

    def get(self, user_id: Union[str, UUID]) -> Union[UserModel, None]:
        user_id = self._hex_str_to_uuid(user_id)

        for user in self._db.find():
            if user["id"] == user_id:
                return UserModel(**user)

    def get_all(self) -> Union[List[UserModel], None]:
        if len(self._db.find()) < 1:
            return []

        users = []
        for user in self._db.find():
            o = UserModel(**user)
            if getattr(o, "deleted_at") and o.deleted_at is not None:
                continue
            else:
                users.append(o)

        return users

    def save(self, user: UserModel) -> UserModel:
        pos = self._get_index(user.id)
        if pos is not None:
            self._db.update(pos, user.to_dict())

        return user

    def find_by_email(self, email: str) -> Union[UserModel, None]:
        for user in self._db.find():
            if user["email"] == email:
                return UserModel(**user)

    def _get_index(self, user_id: Union[str, UUID]):
        user_id = self._hex_str_to_uuid(user_id)

        for idx, user in enumerate(self._db.find()):
            if user["id"] == user_id:
                return idx

    def _find_by_email_or_id(
        self, email: str, user_id: Union[str, UUID]
    ) -> Union[UserModel, None]:
        user_id = self._hex_str_to_uuid(user_id)

        for user in self._db.find():
            if user["email"] == email or user["id"] == user_id:
                return UserModel(**user)

    @staticmethod
    def _hex_str_to_uuid(user_id: Union[str, UUID]) -> UUID:
        if isinstance(user_id, str):
            return UUID(user_id)
        return user_id
