from flask_apispec.views import MethodResource
from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    description = fields.Str()


class BaseResource(MethodResource):
    pass
