from gevent import monkey

monkey.patch_all()

import logging
import multiprocessing

import falcon
import gunicorn.app.base

from app import configure, create_app, start
from app.config import settings


class Application(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(Application, self).__init__()

    def load_config(self):
        config = dict(
            [
                (key, value)
                for key, value in self.options.items()
                if key in self.cfg.settings and value is not None
            ]
        )
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def init_app() -> falcon.App:
    configure()
    return create_app()


def _post_fork(server=None, w=None):
    _config_logging()
    start()


def _config_logging():
    for logger in "gunicorn.access", "gunicorn.error":
        logging.getLogger(logger).propagate = True
        logging.getLogger(logger).handlers = []


if __name__ == "__main__":
    app = init_app()
    env_name = settings.get("ENV_NAME")
    default_workers = (multiprocessing.cpu_count() * 2) + 1
    opts = {
        "accesslog": settings.get("ACCESS_LOG"),
        "access_log_format": settings.get("ACCESS_LOG_FORMAT"),
        "bind": settings.get("BIND"),
        "errorlog": settings.get("ERROR_LOG"),
        "keepalive": settings.get("KEEP_ALIVE"),
        "post_fork": _post_fork,
        "proc_name": settings.get("APP_NAME"),
        "max_requests": settings.get("MAX_REQUESTS"),
        "max_requests_jitter": settings.get("MAX_REQUESTS_JITTER"),
        "worker_class": settings.get("WORKER_CLASS"),
        "workers": settings.get("WORKERS")
        or (1 if env_name == "LOCAL" else default_workers),
    }

    Application(app, opts).run()
