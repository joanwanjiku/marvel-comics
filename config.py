import os

class Config:
    pass


class ProdConfg(Config):
    """
    configurations for prod environment inherits from Config
    """
    pass
class TestConfig(Config):
    pass

class DevConfig(Config):
    """
    configurations for dev environment inherits from Config
    """
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfg,
    'test': TestConfig
}