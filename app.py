import os

import sentry_sdk
from flask_apispec import FlaskApiSpec
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

import config as c

from example import example_bp
from example import routes as example_routes

from extensions import db, logger
from spec import APISPEC_SPEC

project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app(for_celery=False):
    """ Application Factory. """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(c)

    # cors
    CORS(app, expose_headers=['Authorization'], resources={'/*': {'origins': c.ORIGINS}})

    register_extensions(app)
    register_blueprints(app)
    register_shell(app)
    register_external(skip_sentry=for_celery)

    if for_celery:
        register_celery(app)

    return app


def register_celery(app):
    from celery.signals import task_postrun

    # Celery db sessions
    # https://bl.ocks.org/twolfson/a1b329e9353f9b575131
    def handle_celery_postrun(retval=None, *args, **kwargs):
        """After each Celery task, teardown our db session"""
        if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
            if not isinstance(retval, Exception):
                db.session.commit()
        # If we aren't in an eager request (i.e. Flask will perform teardown), then teardown
        if not app.config['CELERY_ALWAYS_EAGER']:
            db.session.remove()

    task_postrun.connect(handle_celery_postrun)


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
    app.config.update({
        'APISPEC_SPEC': APISPEC_SPEC
    })
    docs = FlaskApiSpec(app)

    # example blueprint
    example_api = Api(example_bp)
    app.register_blueprint(example_bp)
    example_routes.set_routes(example_api, docs)
    # add more blueprints below


def register_external(skip_sentry=False):
    """ Register external integrations. """
    # sentry
    if len(c.SENTRY_DSN) == 0:
        logger.warn('Sentry DSN not set.')
    elif skip_sentry:
        logger.info('Skipping Sentry Initialization for Celery.')
    else:
        sentry_sdk.init(c.SENTRY_DSN, integrations=[FlaskIntegration(), RedisIntegration(), SqlalchemyIntegration()])
    # add more external integrations below
