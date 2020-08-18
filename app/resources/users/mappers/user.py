from typing import List, Union

from xid import XID

from app.data.mapper import Mapper
from ..models import UserModel


class UserMapper(Mapper):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, user: UserModel) -> UserModel:
        exists = self._find_by_email_or_id(user.email, user.id)
        if exists:
            raise ValueError

        self._db.users.insert(user.to_dict())

        return self.find(user.id)

    def find(
        self, user_id: Union[XID, None] = None
    ) -> Union[UserModel, List[UserModel], None]:
        if user_id:
            for user in self._db.users.find():
                if user["id"] == user_id:
                    return UserModel(**user)

        if len(self._db.users.find()) < 1:
            return []

        users = []
        for user in self._db.users.find():
            o = UserModel(**user)
            if getattr(o, "deleted_at") and o.deleted_at is not None:
                continue
            else:
                users.append(o)

        return users

    def find_by_email(self, email: str) -> Union[UserModel, None]:
        for user in self._db.users.find():
            if user["email"] == email:
                return UserModel(**user)

    def update(self, user: UserModel) -> UserModel:
        pos = self._get_index(user.id)
        if pos is not None:
            self._db.users.update(pos, user.to_dict())

        return user

    def delete(self, user: UserModel):
        pos = self._get_index(user.id)
        if pos is not None:
            self._db.users.update(pos, user.to_dict())

    def _get_index(self, user_id: XID):
        for idx, user in enumerate(self._db.users.find()):
            if user["id"] == user_id:
                return idx

    def _find_by_email_or_id(self, email: str, user_id: XID) -> Union[UserModel, None]:
        for user in self._db.users.find():
            if user["email"] == email or user["id"] == str(user_id):
                return UserModel(**user)
