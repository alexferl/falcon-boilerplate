try:
    import rapidjson as json
except ImportError:
    import json


def dump(obj, stream, *args, **kwargs):
    return json.dump(obj, stream, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    return json.dumps(obj, *args, **kwargs)


def load(stream, *args, **kwargs):
    return json.load(stream, *args, **kwargs)


def loads(string, *args, **kwargs):
    return json.loads(string, *args, **kwargs)
