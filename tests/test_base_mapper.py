import falcon
import pytest

from app.data import retrieve_model
from app.data.db import setup
from app.data.mapper import Mapper
from app.util.error import HTTPError


class NotImplementedMapper(Mapper):
    pass


def test_mapper_not_implemented():
    db = setup()
    mapper = NotImplementedMapper(db)
    with pytest.raises(NotImplementedError):
        mapper.insert(None)
    with pytest.raises(NotImplementedError):
        mapper.find(None)
    with pytest.raises(NotImplementedError):
        mapper.update(None)
    with pytest.raises(NotImplementedError):
        mapper.delete(None)


class MyMapper(Mapper):
    def __init__(self, db):
        super().__init__(db)
        self.model = None

    def insert(self, model):
        pass

    def find(self, xid):
        return self.model

    def update(self, model):
        pass

    def delete(self, xid):
        pass


@pytest.fixture
def mapper():
    db = setup()
    return MyMapper(db)


def test_resolve_obj_raises_not_found(mapper):
    with pytest.raises(HTTPError) as excinfo:
        retrieve_model(None, mapper)

    assert excinfo.value.status == falcon.HTTP_NOT_FOUND


def test_resolve_object_raises_gone(mapper, model):
    with pytest.raises(HTTPError) as excinfo:
        model.deleted_at = "123"
        mapper.model = model
        retrieve_model(None, mapper)

    assert excinfo.value.status == falcon.HTTP_GONE


def test_resolve_obj_returns_obj(mapper, model):
    mapper.model = model
    result = retrieve_model(None, mapper)

    assert result == model
