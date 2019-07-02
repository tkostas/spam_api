import os
from dotenv import load_dotenv


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


config_factory = {
    'default': Config
}
