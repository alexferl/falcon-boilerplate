import rapidjson


def dump(obj: object, stream: bytes, *args, **kwargs) -> bytes:
    return rapidjson.dump(obj, stream, *args, **kwargs)


def dumps(obj: object, *args, **kwargs) -> bytes:
    return rapidjson.dumps(obj, *args, **kwargs)


def load(stream: bytes, *args, **kwargs) -> dict:
    return rapidjson.load(stream, *args, **kwargs)


def loads(string: str, *args, **kwargs) -> dict:
    return rapidjson.loads(string, *args, **kwargs)
