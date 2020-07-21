from flask import Flask
from flask_bootstrap import Bootstrap

from config import config_options





bootstrap = Bootstrap()


def create_app(config_name):
    # initialize app
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    


    # register blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)
    

    return app