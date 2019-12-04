from extensions import BaseModel, db


class BaseDBModel(BaseModel, db.Model):
    __abstract__ = True
