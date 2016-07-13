import logging.config


def setup_logging(level='INFO'):
    if level is not None:
        fmt = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
        config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': fmt,
                    'datefmt': '%Y-%m-%d %H:%M:%S %z'
                }
            },
            'handlers': {
                'console': {
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler'
                }
            },
            'loggers': {
                '': {
                    'handlers': ['console'],
                    'level': level,
                    'propagate': True
                },
                'gunicorn.error': {
                    'propagate': True
                },
                'gunicorn.access': {
                    'propagate': True
                }
            }
        }

        logging.config.dictConfig(config)
