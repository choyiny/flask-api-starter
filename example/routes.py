from flask_restful import Api

from example.controllers import ExampleIndexController


def set_routes(api: Api):
    """ Setup the routes required for this blueprint. """
    api.add_resource(ExampleIndexController, '/')
