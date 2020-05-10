from app.media import json


def test_create(model):
    assert model.created_at is not None


def test_delete(model):
    model.delete()

    assert model.deleted_at is not None


def test_update(model):
    doc = {"k": "v"}
    model.update(doc)

    assert model.updated_at is not None
    assert model.k == "v"


def test_from_dict(model):
    doc = {"k": "v"}
    model.from_dict(doc)

    assert model.k == doc["k"]


def test_from_json(model):
    doc = {"k": "v"}
    d = json.dumps(doc)
    model.from_json(d)

    assert model.k == doc["k"]


def test_to_dict(model):
    model.k = "v"
    result = model.to_dict()

    assert result["k"] == "v"


def test_to_json(model):
    model.k = "v"
    result = model.to_json()

    assert json.loads(result)["k"] == "v"
