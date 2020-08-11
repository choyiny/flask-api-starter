from extensions import db


class User(db.Model):
    __tablename__ = "users"

    # id
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    name = db.Column(db.String, nullable=False)

    is_admin = db.Column(db.Boolean, nullable=False, default=False)
