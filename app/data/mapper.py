import abc
from typing import List

from xid import XID

from .model import Model


class Mapper(metaclass=abc.ABCMeta):
    def __init__(self, db):
        self._db = db

    def insert(self, model: Model) -> Model:
        raise NotImplementedError()

    def find(self, xid: XID | None) -> Model | List[Model] | None:
        raise NotImplementedError()

    def update(self, model: Model):
        raise NotImplementedError()

    def delete(self, xid: XID):
        raise NotImplementedError()
