"""
Example REST endpoints for a model User.

These endpoints can be reached at /example/users/.
"""
from flask_apispec import marshal_with, use_kwargs, doc
from marshmallow import Schema, fields

from helpers import ErrorResponseSchema

from .example_base_resource import ExampleBaseResource
from ..models import User
from ..schemas import UserSchema, PostUserSchema


@doc(description="""User collection related operations""",)
class UsersResource(ExampleBaseResource):
    @marshal_with(PostUserSchema)
    @use_kwargs(UserSchema)
    def post(self, **user_info):
        """
        Create a new User.
        """
        user = User(**user_info).save()

        return user

    class UserIndexSchema(Schema):
        users = fields.List(fields.Nested(UserSchema))

    @marshal_with(UserIndexSchema)
    def get(self):
        """
        Return a paginated list of users.
        """
        users = User.objects.all()
        return {"users": users}


@doc(description="""User element related operations""",)
class UserResource(ExampleBaseResource):
    @marshal_with(UserSchema)
    def get(self, user_id):
        """
        Return User that matches user_id.
        """
        user = User.objects(id=user_id).first()
        if user is None:
            return {"description": "User not found."}, 404

        return user

    @marshal_with(PostUserSchema)
    @use_kwargs(UserSchema)
    def patch(self, **kwargs):
        """
        Replace attributes for User that matches user_id.
        """
        # modify the user id
        user = User(**kwargs)
        user.name = kwargs.get("name")
        user.save()

        return user

    @marshal_with(ErrorResponseSchema, code=404)
    def delete(self, user_id):
        """
        Delete User that matches user_id.
        """
        user = User.objects(id=user_id).first()
        if user is None:
            return {"description": "User not found."}, 404

        return user
