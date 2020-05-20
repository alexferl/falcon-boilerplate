import falcon

import abc
from typing import List, Union

from app.data.model import Model
from app.util.error import HTTPError


class Mapper(metaclass=abc.ABCMeta):
    def __init__(self, db):
        self._db = db

    def create(self, obj: Model) -> Model:
        raise NotImplementedError()

    def get(self, id_: str) -> Union[Model, None]:
        raise NotImplementedError()

    def get_all(self) -> Union[List[Model], None]:
        raise NotImplementedError()

    def save(self, obj: Model):
        raise NotImplementedError()


def resolve_obj(id_: str, mapper: Mapper) -> Model:
    name = mapper.__class__.__name__.lower().split("mapper")[0].capitalize()
    obj = mapper.get(id_)

    if obj is None:
        raise HTTPError(falcon.HTTP_BAD_REQUEST, f"{name} not found")
    elif obj.deleted_at is not None:
        raise HTTPError(falcon.HTTP_GONE, f"{name} was deleted")

    return obj
