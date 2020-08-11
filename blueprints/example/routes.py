from flask_apispec import FlaskApiSpec
from flask_restful import Api

from blueprints.example import bp_name
from blueprints.example.controllers import (
    UsersCollectionController,
    UsersController,
)


def set_routes(api: Api, docs: FlaskApiSpec):
    """ Setup the routes required for this blueprint. """

    resource_to_route = [
        (UsersCollectionController, "/users/"),
        (UsersController, "/users/<string:user_id>"),
    ]

    for controller, route in resource_to_route:
        api.add_resource(controller, route)
        docs.register(controller, blueprint=bp_name)
