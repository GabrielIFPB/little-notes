from flask import Flask
from flask_login import LoginManager

from little_notes.ext.db.models import User

from .main import blueprint

login_manager = LoginManager()


def init_app(app: Flask):
    login_manager.init_app(app=app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id: int):
        return User.query.get(int(user_id))

    app.register_blueprint(blueprint=blueprint)
