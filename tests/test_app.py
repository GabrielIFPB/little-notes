from flask import Flask


def test_app_created(app: Flask):
    assert app.name == "little_notes.app"


def test_app_debug(app: Flask):
    assert app.debug is True


def test_config_is_loaded(config):
    assert config["DEBUG"] is True
    assert config["SQLALCHEMY_TRACK_MODIFICATIONS"] is True
    assert config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] is True
    assert config["DEBUG_TB_PROFILER_ENABLED"] is True
