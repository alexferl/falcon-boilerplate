from app.data.model import Model


class UserModel(Model):
    email: str = ""
    first_name: str = ""
    last_name: str = ""
