import logging

logger = logging.getLogger('app.util.serialization')

try:
    import ujson as json
except ImportError:
    logger.warning('ujson is not installed, using standard json module')
    import json


def loads(data):
    return json.loads(data)


def dumps(data):
    return json.dumps(data)
