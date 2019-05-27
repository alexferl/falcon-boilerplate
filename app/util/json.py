try:
    import rapidjson as json
except ImportError:
    import json


def loads(data):
    return json.loads(data)


def dumps(data):
    return json.dumps(data)
