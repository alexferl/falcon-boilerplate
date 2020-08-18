import falcon

from xid import XID

from app.util.error import HTTPError
from .mapper import Mapper
from .model import Model


def retrieve_model(xid: XID, mapper_: Mapper) -> Model:
    name = mapper_.__class__.__name__.lower().split("mapper")[0].capitalize()
    model = mapper_.find(xid)

    if model is None:
        raise HTTPError(falcon.HTTP_NOT_FOUND, f"{name} not found")
    elif model.deleted_at is not None:
        raise HTTPError(falcon.HTTP_GONE, f"{name} was deleted")

    return model
