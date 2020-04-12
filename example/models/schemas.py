from flask_marshmallow.sqla import ModelSchema

from example.models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
