"""
Example REST endpoints for a model User.

These endpoints can be reached at /example/users/.
"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from example.models import User, UserSchema
from extensions import db


class UsersCollectionController(Resource):
    """
    /users/
    """
    def post(self):
        """
        Create a new User.
        """
        json = request.get_json(force=True)
        if not json:
            return {'success': False}, 400
        try:
            user = UserSchema().load(json, session=db.session)
        except ValidationError as e:
            return e, 422

        db.session.add(user)
        db.session.commit()

        return UserSchema().dump(user)

    def get(self):
        """
        Return a paginated list of users.
        """
        users = User.query.all()
        return {
            'data': UserSchema(many=True).dump(users)
        }


class UsersController(Resource):
    """
    /users/<string:user_id>
    """
    def get(self, user_id):
        """
        Return User that matches user_id.
        """
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return {'success': False}, 404

        return UserSchema().dump(user)

    def put(self, user_id):
        """
        Replace attributes for User that matches user_id.
        """
        json = request.get_json(force=True)
        if not json:
            return {'success': False}, 400
        try:
            user = UserSchema().load(json, session=db.session)
        except ValidationError as e:
            return e, 422

        # modify the user id
        user.user_id = user_id

        db.session.add(user)
        db.session.commit()

        return UserSchema().dump(user)

    def delete(self, user_id):
        """
        Delete User that matches user_id.
        """
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return {'success': False}, 404

        db.session.delete(user)
        db.session.commit()

        return {'success': True}
