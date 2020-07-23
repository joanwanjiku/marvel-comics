import os

class Config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'



class ProdConfg(Config):
    """
    configurations for prod environment inherits from Config
    """
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bryson:0987@localhost/marvel'


class DevConfig(Config):
    """
    configurations for dev environment inherits from Config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bryson:0987@localhost/marvel'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfg,
    'test': TestConfig
}