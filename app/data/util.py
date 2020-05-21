import falcon

from app.util.error import HTTPError
from .mapper import Mapper
from .model import Model


def retrieve_obj(id_: str, mapper_: Mapper) -> Model:
    name = mapper_.__class__.__name__.lower().split("mapper")[0].capitalize()
    obj = mapper_.get(id_)

    if obj is None:
        raise HTTPError(falcon.HTTP_BAD_REQUEST, f"{name} not found")
    elif obj.deleted_at is not None:
        raise HTTPError(falcon.HTTP_GONE, f"{name} was deleted")

    return obj
