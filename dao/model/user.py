from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dao.model import GenreSchema
from setup_db import db


class User(db.Model):
    """
    User model
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    surname = Column(String)
    favorite_genre = Column(Integer, ForeignKey("genre.id"))

    genre = relationship("Genre")


class UserSchema(Schema):
    """
    User schema for serialize
    """
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()

    genre = fields.Nested(GenreSchema)
