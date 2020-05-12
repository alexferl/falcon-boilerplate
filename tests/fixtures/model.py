import pytest

from app.data.model import BaseModel, Model


class NestedModel(BaseModel):
    field2: str = ""


class MyModel(Model):
    field1: str = ""
    nested: NestedModel = NestedModel()


@pytest.fixture
def model():
    return MyModel()
