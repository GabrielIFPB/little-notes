from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def init_app(app: Flask) -> None:
    DebugToolbarExtension(app)
