import falcon

import abc
from typing import List, Union

from app.data.model import BaseModel
from app.util.error import HTTPError


class BaseMapper(metaclass=abc.ABCMeta):
    def create(self, obj: BaseModel) -> BaseModel:
        raise NotImplementedError()

    def get(self, id: str) -> Union[BaseModel, None]:
        raise NotImplementedError()

    def get_all(self) -> Union[List[BaseModel], None]:
        raise NotImplementedError()

    def save(self, obj: BaseModel):
        raise NotImplementedError()


def resolve_obj(id: str, mapper: BaseMapper) -> BaseModel:
    name = mapper.__class__.__name__.lower().split("mapper")[0].capitalize()
    obj = mapper.get(id)

    if obj is None:
        raise HTTPError(falcon.HTTP_BAD_REQUEST, f"{name} not found")
    elif obj.deleted_at is not None:
        raise HTTPError(falcon.HTTP_GONE, f"{name} was deleted")

    return obj
