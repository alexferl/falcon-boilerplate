from typing import Dict

import rapidjson
from xid import XID

from app.config import settings


def xid_encoder(obj):
    if isinstance(obj, XID):
        return str(obj)
    else:
        raise ValueError("%r is not JSON serializable" % obj)


def dump(obj: object, stream: bytes, *args, **kwargs) -> bytes:
    kwargs = add_settings_to_kwargs(kwargs)
    if "default" not in kwargs:
        kwargs["default"] = xid_encoder
    return rapidjson.dump(obj, stream, *args, **kwargs)


def dumps(obj: object, *args, **kwargs) -> bytes:
    kwargs = add_settings_to_kwargs(kwargs)
    if "default" not in kwargs:
        kwargs["default"] = xid_encoder
    return rapidjson.dumps(obj, *args, **kwargs)


def load(stream: bytes, *args, **kwargs) -> Dict:
    kwargs = add_settings_to_kwargs(kwargs)
    return rapidjson.load(stream, *args, **kwargs)


def loads(string: str, *args, **kwargs) -> Dict:
    kwargs = add_settings_to_kwargs(kwargs)
    return rapidjson.loads(string, *args, **kwargs)


def add_settings_to_kwargs(kwargs: Dict[str, str]) -> Dict[str, str]:
    json_datetime_mode = settings.get("JSON_DATETIME_MODE")
    json_number_mode = settings.get("JSON_NUMBER_MODE")
    json_uuid_mode = settings.get("JSON_UUID_MODE")

    datetime_mode = (
        getattr(rapidjson, json_datetime_mode)
        if hasattr(rapidjson, json_datetime_mode or "")
        else None
    )
    number_mode = (
        getattr(rapidjson, json_number_mode)
        if hasattr(rapidjson, json_number_mode or "")
        else None
    )
    uuid_mode = (
        getattr(rapidjson, json_uuid_mode)
        if hasattr(rapidjson, json_uuid_mode or "")
        else None
    )

    if "datetime_mode" not in kwargs:
        kwargs["datetime_mode"] = datetime_mode

    if "number_mode" not in kwargs:
        kwargs["number_mode"] = number_mode

    if "uuid_mode" not in kwargs:
        kwargs["uuid_mode"] = uuid_mode

    return kwargs
