from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, List
from uuid import UUID


def setup(clear: bool = False) -> _InMemDB:
    if clear is True:
        global _data
        _data = {}

    return _InMemDB()


_data = {
    "users": [
        {
            "id": UUID("a6b2cb86-c689-40bb-9d5a-44b9bc096d89"),
            "created_at": datetime(2020, 5, 9, 16, 20, 40, 560920),
            "first_name": "Alain",
            "last_name": "Belanger",
            "email": "alain.belanger@example.com",
        },
        {
            "id": UUID("8307e8d2-e225-4ee3-8606-f7f2d01fdaf1"),
            "created_at": datetime(2020, 5, 9, 16, 21, 1, 326478),
            "first_name": "Sylvie",
            "last_name": "Boucher",
            "email": "sylvie.boucher@example.com",
        },
    ]
}


class _InMemDB:
    def __getattr__(self, item: str) -> _Collection:
        return _Collection(item)


class _Collection:
    def __init__(self, name: str):
        global _data
        self._data = _data

        self.name = name
        if self.name not in self._data:
            self._data[self.name] = []

    def insert(self, data: Dict[str, Any]):
        self._data[self.name].append(data)

    def update(self, id_: int, data: Dict[str, Any]):
        self._data[self.name][id_] = data

    def find(self) -> List[Dict]:
        return self._data[self.name]
