class BaseConfig(object):
    APP_NAME = 'app'
    ENV = None
    LOG_LEVEL = 'INFO'


class DevConfig(BaseConfig):
    ENV = 'DEV'
    LOG_LEVEL = 'DEBUG'


class ProdConfig(BaseConfig):
    ENV = 'PROD'


configs = DevConfig
