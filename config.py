import os
from instance.config import SECRET_KEY

class Config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SECRET_KEY = SECRET_KEY
    UPLOADED_PHOTOS_DEST = 'app/static/photos'



class ProdConfg(Config):
    """
    configurations for prod environment inherits from Config
    """
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:#Saintropez1@localhost/marvel'


class DevConfig(Config):
    """
    configurations for dev environment inherits from Config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:#Saintropez1@localhost/marvel'
    SECRET_KEY = SECRET_KEY
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfg,
    'test': TestConfig
}