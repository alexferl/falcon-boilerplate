import logging
import logging.config

from app.config import settings


class GunicornFilter(logging.Filter):
    def filter(self, record):
        # workaround to remove the duplicate access log
        if '"- - HTTP/1.0" 0 0' in record.msg:
            return False
        else:
            return True


def setup_logging():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "gunicorn_filter": {
                "()": GunicornFilter
            }
        },
        "formatters": {
            "standard": {
                "format": settings.get("LOG_FORMAT"),
                "datefmt": settings.get("LOG_DATE_FORMAT")
            }
        },
        "handlers": {
            "console": {
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "filters": ["gunicorn_filter"],
            }
        },
        "loggers": {
            "": {
                "handlers": settings.get("LOG_HANDLERS").split(','),
                "level": settings.get("LOG_LEVEL")
            }
        }
    }

    logging.config.dictConfig(config)
