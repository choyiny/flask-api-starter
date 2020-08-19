from mongoengine import Document, StringField, BooleanField


class User(Document):

    name = StringField(required=True)

    is_admin = BooleanField(default=False)
