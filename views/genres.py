from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres, 200

    def post(self):
        data = request.json
        genre_service.create(data)
        added_genre_id = genre_service.create(data)
        return "added!", 201, {'location': f'/movies/{added_genre_id}'}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre, 200

    def put(self, gid):
        data = request.json
        genre_service.update(data, gid)
        return "updated!", 204

    def patch(self, gid):
        data = request.json
        genre_service.update(data, gid)
        return "partial updated!", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "deleted", 204
