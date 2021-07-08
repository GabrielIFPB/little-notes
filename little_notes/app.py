from flask import Flask

from little_notes.ext import config


def create_app() -> Flask:
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app=app)
    return app


# if __name__ == "__main__":
#     create_app().run(
#         "127.0.0.1", 5000, debug=True, use_reloader=True, use_debugger=True
#     )
