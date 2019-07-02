import os
from flask import Flask

from config import config_factory

from app.site import site as site_bp


def create_app(config_name=os.getenv('APP_ENV', 'default')):
    app = Flask(__name__)
    app.config.from_object(config_factory[config_name])

    app.register_blueprint(site_bp)

    return app
