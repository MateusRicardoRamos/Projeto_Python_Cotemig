from sqlalchemy.ext.declarative import declared_attr

from . import db


class ModeloBase(db.Model):
    __abstract__ = True

    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)
