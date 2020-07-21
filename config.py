import os
from dotenv import load_dotenv
load_dotenv()
from instance.config import DATABASE_URL, SECRET_KEY

class Config:
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    #SECRET_KEY= os.environ.get("SECRET_KEY")
    SECRET_KEY = SECRET_KEY 
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}