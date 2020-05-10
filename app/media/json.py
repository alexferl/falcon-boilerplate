try:
    import rapidjson as json
except ImportError:  # pragma: no cover
    import json


def dump(obj: object, stream: bytes, *args, **kwargs) -> bytes:
    return json.dump(obj, stream, *args, **kwargs)


def dumps(obj: object, *args, **kwargs) -> bytes:
    return json.dumps(obj, *args, **kwargs)


def load(stream: bytes, *args, **kwargs) -> dict:
    return json.load(stream, *args, **kwargs)


def loads(string: str, *args, **kwargs) -> dict:
    return json.loads(string, *args, **kwargs)
