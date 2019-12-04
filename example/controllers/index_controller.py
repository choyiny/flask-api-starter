from flask_restful import Resource


class ExampleIndexController(Resource):

    def get(self):
        return {'version': 1.0, 'title': 'Example Blueprint'}
