import falcon
import pytest

from app.data.mapper import BaseMapper, resolve_obj
from app.util.error import HTTPError


class NotImplementedMapper(BaseMapper):
    pass


def test_mapper_not_implemented():
    mapper = NotImplementedMapper()
    with pytest.raises(NotImplementedError):
        mapper.create(None)
    with pytest.raises(NotImplementedError):
        mapper.get("")
    with pytest.raises(NotImplementedError):
        mapper.get_all()
    with pytest.raises(NotImplementedError):
        mapper.save(None)


class MyMapper(BaseMapper):
    def __init__(self):
        self.model = None

    def create(self, obj):
        pass

    def get(self, id):
        return self.model

    def get_all(self):
        pass

    def save(self, obj):
        pass


@pytest.fixture
def mapper():
    return MyMapper()


def test_resolve_obj_raises_bad_request(mapper):
    with pytest.raises(HTTPError) as excinfo:
        resolve_obj("", mapper)

    assert excinfo.value.status == falcon.HTTP_BAD_REQUEST


def test_resolve_object_raises_gone(mapper, model):
    with pytest.raises(HTTPError) as excinfo:
        model.deleted_at = "123"
        mapper.model = model
        resolve_obj("", mapper)

    assert excinfo.value.status == falcon.HTTP_GONE


def test_resolve_obj_returns_obj(mapper, model):
    mapper.model = model
    result = resolve_obj("", mapper)

    assert result == model
