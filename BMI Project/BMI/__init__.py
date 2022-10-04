# this init is used for initialization of the application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db=SQLAlchemy()


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])

    from BMI.views import mod as users_module 
    db.init_app(app)    
    app.register_blueprint(users_module)
    return app

