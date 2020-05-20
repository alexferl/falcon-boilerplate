from app.data.db import _InMemDB, setup


def test_db_setup():
    db = setup()

    assert isinstance(db, _InMemDB)


def test_lazy_create_collection():
    db = setup(True)
    db.lazy.find()

    assert db.lazy._data["lazy"] == []


def test_insert():
    db = setup(True)
    data = {"test": "data"}
    db.test.insert(data)

    assert db.test._data["test"] == [data]


def test_update():
    db = setup(True)
    data = {"test2": "data"}
    db.test.insert(data)
    db.test.update(0, {"test2": "data2"})

    assert db.test._data["test"] == [{"test2": "data2"}]


def test_find():
    db = setup(True)
    data1 = {"test": "data1"}
    data2 = {"test": "data2"}
    db.test.insert(data1)
    db.test.insert(data2)

    assert db.test.find() == [data1, data2]
