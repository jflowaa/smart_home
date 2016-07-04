import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    from .device import device as device_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(device_blueprint, url_prefix="/device")
    print(app.url_map)
    return app

if __name__ == '__main__':
    manager.run()