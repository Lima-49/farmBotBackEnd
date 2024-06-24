from flask import Flask
from app.config import Config
from app.controllers import main

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config())
    app.register_blueprint(main)

    return app
