from app.media import json
from tests.fixtures.model import MyModel

doc = {"field1": "value1", "nested": {"field2": "value2"}}


def test_create():
    model = MyModel(**doc)

    assert model.created_at is not None
    assert model.field1 == doc["field1"]
    assert model.nested.field2 == "value2"


def test_delete(model):
    model.delete()

    assert model.deleted_at is not None


def test_update(model):
    updated = model.update({"field1": "value3", "nested": {"field2": "value4"}})

    assert updated.updated_at is not None
    assert updated.field1 == "value3"
    assert updated.nested.field2 == "value4"


def test_to_dict(model):
    model.field1 = "value1"
    model.nested.field2 = "value2"
    result = model.to_dict()

    assert result["field1"] == "value1"
    assert result["nested"]["field2"] == "value2"


def test_to_json(model):
    model.field1 = "value1"
    model.nested.field2 = "value2"
    result = json.loads(model.to_json())

    assert result["field1"] == "value1"
    assert result["nested"]["field2"] == "value2"
