from __future__ import annotations
from datetime import datetime

from pydantic import BaseModel, Field
from xid import XID

from app.media import json

BaseModel = BaseModel


class Model(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    id: XID = Field(default_factory=XID)
    created_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime = None
    updated_at: datetime = None

    def delete(self):
        self.deleted_at = datetime.now()

    def update(self, d: dict) -> Model:
        d["updated_at"] = datetime.now()
        o = self.to_dict()
        o.update(d)
        return self.parse_obj(o)

    def to_dict(self) -> dict:
        return self.dict()

    def to_json(self) -> bytes:
        return json.dumps(self.to_dict())
