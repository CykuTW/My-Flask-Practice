from flask import Flask
from flask.cli import FlaskGroup
import controllers
import click

from models import db
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# Register blueprints
app.register_blueprint(controllers.index.blueprint)


# For development with Flask Click

def create_app(info=None):
    return app

cli = FlaskGroup(create_app=create_app)

@cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Initialize the database')
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    cli()