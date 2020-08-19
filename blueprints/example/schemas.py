from marshmallow import Schema, fields


class PostUserSchema(Schema):
    name = fields.Str()
    is_admin = fields.Bool()


class UserSchema(PostUserSchema):
    id = fields.Str()
