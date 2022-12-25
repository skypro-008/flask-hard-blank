from flask import request
from flask_restx import Resource, Namespace

from setup_db import db
from dao.genre import GenreDAO
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_dao = GenreDAO(db.session)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_dao.get_all()
        genres_serialize = GenreSchema().dump(genres, many=True)
        return genres_serialize, 200

    def post(self):
        data = request.json
        genre_dao.create(data)
        return "added!", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genres = genre_dao.get_one(gid)
        genres_serialize = GenreSchema().dump(genres)
        return genres_serialize, 200

    def put(self, gid):
        data = request.json
        genre_dao.update(data, gid)
        return "updated!", 204

    def patch(self, gid):
        data = request.json
        genre_dao.update(data, gid)
        return "partial updated!", 204

    def delete(self, gid):
        genre_dao.delete(gid)
        return "deleted", 204
