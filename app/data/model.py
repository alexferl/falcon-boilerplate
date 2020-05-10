from __future__ import annotations
from dataclasses import asdict, field, dataclass

from app.media import json
from app.util.date import get_isoformat


@dataclass
class BaseModel:
    id: str = ""
    created_at: str = field(default_factory=get_isoformat)
    deleted_at: str = None
    updated_at: str = None

    def _set_attrs(self, d: dict) -> BaseModel:
        for k, v in d.items():
            setattr(self, k, v)
        return self

    def delete(self):
        self.deleted_at = get_isoformat()

    def update(self, d: dict) -> BaseModel:
        self.updated_at = get_isoformat()
        return self._set_attrs(d)

    def from_dict(self, d: dict) -> BaseModel:
        return self._set_attrs(d)

    def from_json(self, d: str) -> BaseModel:
        return self._set_attrs(json.loads(d))

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> bytes:
        return json.dumps(self.to_dict())
