from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """
    User model
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)


class UserSchema(Schema):
    """
    User schema for serialize
    """
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
