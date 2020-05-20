from __future__ import annotations
from datetime import datetime
from uuid import UUID


def setup() -> InMemDB:
    return InMemDB()


_data = [
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


class InMemDB:
    def __init__(self):
        global _data
        self._data = _data

    def insert(self, data):
        self._data.append(data)

    def update(self, id_, data):
        self._data[id_] = data

    def find(self):
        return self._data
