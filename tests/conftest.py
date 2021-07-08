import pytest
from flask import Flask, template_rendered

from little_notes.app import create_app
from little_notes.ext.db import db as _db


@pytest.fixture(scope="module")
def app(request) -> Flask:
    """Session-wide test `Flask` application."""
    app = create_app()
    context = app.app_context()
    context.push()

    def teardown():
        context.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="module")
def db(app, request):
    """Session-wide test database."""
    _db.init_app(app=app)

    def teardown():
        _db.drop_all()

    _db.create_all()
    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)
    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="module")
def captured_templates(app, request):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)

    def teardown():
        template_rendered.disconnect(record, app)

    request.addfinalizer(teardown)
    return recorded


@pytest.fixture(scope="module")
def runner(app):
    return app.test_cli_runner()
