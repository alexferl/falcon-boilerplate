from dataclasses import dataclass

import pytest

from app.data.model import BaseModel


@dataclass
class MyModel(BaseModel):
    k: str = ""


@pytest.fixture
def model():
    return MyModel()
