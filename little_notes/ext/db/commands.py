import click

from little_notes.ext.db import db

# from little_notes.ext.db.models import User


def create_db():
    """Creates database"""
    db.create_all()
    click.echo("Tables created successfully.")


def drop_db():
    """Cleans database"""
    db.drop_all()
    click.echo("Tables successfully deleted.")


def populate_db():
    """Populate the database customer table with sample data"""
    # data = [
    #     User(name="gustavo"),
    #     User(name="josefa"),
    # ]
    # db.session.bulk_save_objects(data)
    # db.session.commit()
    # click.echo(f"Customers: {User.query.all()}")
    click.echo("users")
    # return Client.query.all()


def users():
    """user list"""
    click.echo("users")
