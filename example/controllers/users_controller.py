"""
Example REST endpoints for a model User.

These endpoints can be reached at /example/users/.
"""
from flask_apispec import marshal_with, use_kwargs, doc

from example.controllers.example_base_controller import ExampleBaseController
from example.models import User
from example.models.schemas import UserSchema
from extensions import db
from helpers import ErrorResponseSchema


@doc(description="""User collection related operations""",)
class UsersCollectionController(ExampleBaseController):
    """
    /users/
    """

    @marshal_with(UserSchema)
    @use_kwargs(UserSchema)
    def post(self, **user_info):
        """
        Create a new User.
        """
        user = User(**user_info)
        db.session.add(user)
        db.session.commit()

        return UserSchema().dump(user)

    @marshal_with(UserSchema(many=True))
    def get(self):
        """
        Return a paginated list of users.
        """
        users = User.query.all()
        return UserSchema(many=True).dump(users)


@doc(description="""User element related operations""",)
class UsersController(ExampleBaseController):
    """
    /users/<string:user_id>
    """

    @marshal_with(UserSchema)
    @marshal_with(ErrorResponseSchema, code=404)
    def get(self, user_id):
        """
        Return User that matches user_id.
        """
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return {"description": "User cannot be found."}, 404

        return UserSchema().dump(user)

    @marshal_with(UserSchema)
    @use_kwargs(UserSchema)
    def put(self, **kwargs):
        """
        Replace attributes for User that matches user_id.
        """
        # modify the user id
        user = User(**kwargs)
        user.user_id = kwargs.get("user_id")

        db.session.add(user)
        db.session.commit()

        return UserSchema().dump(user)

    @marshal_with(ErrorResponseSchema, code=404)
    def delete(self, user_id):
        """
        Delete User that matches user_id.
        """
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return {"description": "User cannot be found."}, 404

        db.session.delete(user)
        db.session.commit()

        return {"description": f"User {user_id} deleted."}
