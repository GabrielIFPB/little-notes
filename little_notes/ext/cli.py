import click
from flask import Flask

from little_notes.ext.db.commands import create_db, drop_db, populate_db, users


def init_app(app: Flask):
    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command("create_db")(create_db))

    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command("drop_db")(drop_db))

    app.cli.add_command(app.cli.command()(populate_db))
    app.cli.add_command(app.cli.command("populate_db")(populate_db))

    app.cli.add_command(app.cli.command()(users))
    app.cli.add_command(app.cli.command("users")(users))

    @app.cli.command()
    def user():
        """users list"""
        click.echo("users")
