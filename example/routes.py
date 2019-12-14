from flask_restful import Api

from example.controllers import ExampleIndexController, UsersCollectionController, UsersController, PraiseController


def set_routes(api: Api):
    """ Setup the routes required for this blueprint. """
    api.add_resource(ExampleIndexController, '/')

    api.add_resource(UsersCollectionController, '/users/')
    api.add_resource(UsersController, '/users/<string:user_id>')

    api.add_resource(PraiseController, '/praise')
