import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "msadfjksjhkjhkj763474hsdjh3789+32/erx(*&@$)"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LOGGING_LOCATION = "site.log"
    LOGGING_LEVEL = logging.DEBUG

    @staticmethod
    def init_app(app):
        handler = logging.FileHandler(app.config["LOGGING_LOCATION"])
        handler.setLevel(app.config["LOGGING_LEVEL"])
        app.logger.addHandler(handler)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')


config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
