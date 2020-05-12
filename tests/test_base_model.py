from app.media import json

doc = {"field1": "value1", "nested": {"field2": "value2"}}


def test_create(model):
    assert model.created_at is not None


def test_delete(model):
    model.delete()

    assert model.deleted_at is not None


def test_update(model):
    model = model.update(doc)

    assert model.updated_at is not None
    assert model.field1 == doc["field1"]
    assert model.nested.field2 == "value2"


def test_from_dict(model):
    model = model.from_dict(doc)

    assert model.field1 == doc["field1"]
    assert model.nested.field2 == "value2"


def test_from_json(model):
    model = model.from_json(json.dumps(doc))

    assert model.field1 == doc["field1"]
    assert model.nested.field2 == "value2"


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
