import os

import mongoengine
import sentry_sdk
from flask import Flask, jsonify
from flask_apispec import FlaskApiSpec
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

import config as c
from extensions import logger
from spec import APISPEC_SPEC

project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app(for_celery=False):
    """ Application Factory. """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(c)

    # cors
    CORS(
        app, expose_headers=["Authorization"], resources={"/*": {"origins": c.ORIGINS}}
    )

    register_extensions()
    register_blueprints(app)
    register_shell(app)
    register_external(skip_sentry=for_celery)

    # Return validation errors as JSON
    @app.errorhandler(422)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    @app.errorhandler(404)
    def handle_404(err):
        return jsonify({"description": "Not Found"}), err.code

    return app


def register_shell(app: Flask):
    """ Expose more attributes to the Flask Shell. """

    @app.shell_context_processor
    def make_shell_context():
        # make below variables accessible in the shell for testing purposes
        return {"app": app}


def register_extensions():
    """ Register Flask extensions. """

    mongoengine.connect(host=c.MONGODB_URL)


def register_blueprints(app: Flask):
    """ Register Flask blueprints. """
    app.config.update({"APISPEC_SPEC": APISPEC_SPEC})
    docs = FlaskApiSpec(app)

    # example blueprint
    from blueprints.example import example_bp
    from blueprints.example import routes as example_routes

    example_routes.set_routes(app, example_bp, docs)


def register_external(skip_sentry=False):
    """ Register external integrations. """
    # sentry
    if len(c.SENTRY_DSN) == 0:
        logger.warn("Sentry DSN not set.")
    elif skip_sentry:
        logger.info("Skipping Sentry Initialization for Celery.")
    else:
        sentry_sdk.init(
            c.SENTRY_DSN,
            integrations=[
                FlaskIntegration(),
                RedisIntegration(),
                SqlalchemyIntegration(),
            ],
        )
