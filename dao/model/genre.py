from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from setup_db import db


class Genre(db.Model):
    """
    Genre model
    """
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String(155))


class GenreSchema(Schema):
    """
    Genre schema for serialize
    """
    id = fields.Int()
    name = fields.Str()
