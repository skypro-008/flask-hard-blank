from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    """
    Director model
    """
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(155))


class DirectorSchema(Schema):
    """
    Director schema for serialize
    """
    id = fields.Int()
    name = fields.Str()
