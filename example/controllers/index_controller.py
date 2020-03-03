from flask_restful import Resource


class ExampleIndexController(Resource):

    def get(self):
        """ An example index page for the API module. """
        return {'version': 1.0, 'title': 'Example Blueprint'}
