import abc
from typing import List, Union

from .model import Model


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
