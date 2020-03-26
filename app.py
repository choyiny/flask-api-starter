import os

import sentry_sdk
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

import config as c

from example import example_bp
from example import routes as example_routes

from extensions import db, logger

project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app():
    """ Application Factory. """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(c)

    # cors
    CORS(app, expose_headers=['Authorization'], resources={'/*': {'origins': c.ORIGINS}})

    register_extensions(app)
    register_blueprints(app)
    register_shell(app)
    register_external()

    return app


def register_shell(app: Flask):
    """ Expose more attributes to the Flask Shell. """
    @app.shell_context_processor
    def make_shell_context():
        # make below variables accessible in the shell for testing purposes
        return {
            'app': app,
            'db': db
        }


def register_extensions(app: Flask):
    """ Register Flask extensions. """

    if len(c.SQLALCHEMY_DATABASE_URI) == 0:
        logger.warn('Database URL not set.')
        return

    db.init_app(app)
    migrate = Migrate(app, db)


def register_blueprints(app: Flask):
    """ Register Flask blueprints. """
    # example blueprint
    example_api = Api(example_bp)
    example_routes.set_routes(example_api)
    app.register_blueprint(example_bp)
    # add more blueprints below


def register_external():
    """ Register external integrations. """
    # sentry
    if len(c.SENTRY_DSN) == 0:
        logger.warn('Sentry DSN not set.')
    else:
        sentry_sdk.init(c.SENTRY_DSN, integrations=[FlaskIntegration()])
    # add more external integrations below
