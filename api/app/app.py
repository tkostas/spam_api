import os
from flask import Flask
from flask_cors import CORS

from app.v1 import api_v1
from config import config_factory


def create_app(config_name=os.getenv('API_ENV', 'default')):
    app = Flask(__name__)
    app.config.from_object(config_factory[config_name])

    CORS(app)

    app.register_blueprint(api_v1, url_prefix='/')
    return app