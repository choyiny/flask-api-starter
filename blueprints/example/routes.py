from flask import Blueprint, Flask
from flask_apispec import FlaskApiSpec

from blueprints.example import bp_name
from blueprints.example.controllers import (
    UsersResource,
    UserResource,
)


def set_routes(app: Flask, bp: Blueprint, docs: FlaskApiSpec):
    # a list of resources
    resources = [
        (UsersResource, "/users/", "users", ["GET", "POST"]),
        (UserResource, "/users/<string:user_id>", "user", ["GET", "PATCH", "DELETE"]),
    ]

    for resource, route, name, methods in resources:
        bp.add_url_rule(route, view_func=resource.as_view(name), methods=methods)

    app.register_blueprint(bp)

    for resource, route, name, methods in resources:
        docs.register(resource, blueprint=bp_name, endpoint=name)
