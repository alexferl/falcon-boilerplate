from dataclasses import dataclass

from app.data.model import BaseModel


@dataclass
class UserModel(BaseModel):
    email: str = ""
    first_name: str = ""
    last_name: str = ""
