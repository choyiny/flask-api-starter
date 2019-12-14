from utils import ExampleClass
from flask_restful import Resource


class PraiseController(Resource):

  def get(self):
    ExampleClass.praise_jordan_liu()
    return {'data': 'Damn, Jordan Liu. You did a great job.'}
