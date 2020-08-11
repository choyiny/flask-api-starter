from flask_apispec.views import MethodResourceMeta
from flask_restful import Resource as RestfulResource, Api
from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    description = fields.Str()


class BaseResource(RestfulResource, metaclass=MethodResourceMeta):
    pass


def add_blueprint(app, docs, bp, bp_routes) -> None:
    api = Api(bp)
    app.register_blueprint(bp)
    bp_routes.set_routes(api, docs)
