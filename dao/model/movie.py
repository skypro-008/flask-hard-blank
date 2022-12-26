from marshmallow import Schema, fields

from setup_db import db


class Movie(db.Model):
    """
    Movie model
    """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(155))
    description = db.Column(db.String(155))
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


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

    genre = fields.Str()
    director = fields.Str()
