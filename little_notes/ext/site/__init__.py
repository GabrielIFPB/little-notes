from flask import Flask

from .main import blueprint


def init_app(app: Flask):
    app.register_blueprint(blueprint=blueprint)
