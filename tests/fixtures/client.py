import pytest
from falcon import testing

from app import configure, create_app


@pytest.fixture
def client():
    configure()
    return testing.TestClient(create_app())
