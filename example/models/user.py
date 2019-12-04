from base.base_model import BaseDBModel
from extensions import db


class User(BaseDBModel):
    __tablename__ = 'users'

    # id
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # name to go by
    name = db.Column(db.String, nullable=False)
