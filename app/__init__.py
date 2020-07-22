from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet, configure_uploads




bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)



def create_app(config_name):
    # initialize app
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    


    # register blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)
    
    configure_uploads(app, photos)

    return app