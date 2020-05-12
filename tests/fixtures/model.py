import pytest
from pydantic import BaseModel

from app.data.model import Model


class NestedModel(BaseModel):
    field2: str = ""


class MyModel(Model):
    field1: str = ""
    nested: NestedModel = NestedModel()


@pytest.fixture
def model():
    return MyModel()
