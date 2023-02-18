from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema
from setup_db import db


class Movie(db.Model):
    """
    Movie model
    """
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    title = Column(String(155))
    description = Column(String(155))
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    director_id = Column(Integer, ForeignKey('director.id'))

    genre = relationship("Genre")
    director = relationship("Director")


class MovieSchema(Schema):
    """
    Movie schema for serialize
    """
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()

    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
