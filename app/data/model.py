from __future__ import annotations

from pydantic import BaseModel, Field

from app.media import json
from app.util.date import get_isoformat


class Model(BaseModel):
    id: str = ""
    created_at: str = Field(default_factory=get_isoformat)
    deleted_at: str = None
    updated_at: str = None

    def delete(self):
        self.deleted_at = get_isoformat()

    def update(self, d: dict) -> Model:
        d["updated_at"] = get_isoformat()
        return self.from_dict(d)

    def from_dict(self, d: dict) -> Model:
        return self.parse_obj(d)

    def from_json(self, d: str) -> Model:
        return self.from_dict(json.loads(d))

    def to_dict(self) -> dict:
        return self.dict()

    def to_json(self) -> bytes:
        return json.dumps(self.to_dict())
