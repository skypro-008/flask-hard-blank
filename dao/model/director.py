from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from setup_db import db


class Director(db.Model):
    """
    Director model
    """
    __tablename__ = "director"

    id = Column(Integer, primary_key=True)
    name = Column(String(155))


class DirectorSchema(Schema):
    """
    Director schema for serialize
    """
    id = fields.Int()
    name = fields.Str()
