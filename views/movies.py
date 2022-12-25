from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters = request.args
        movies = movie_service.get_all(filters)
        return movies, 200

    def post(self):
        data = request.json
        added_movie_id = movie_service.create(data)
        return f"{data.get('title')} was added!", 201, {'location': f'/movies/{added_movie_id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie, 200

    def put(self, mid):
        data = request.json
        movie_service.update(data, mid)
        return f"{data['title']} was updated!", 204

    def patch(self, mid):
        data = request.json
        movie_service.update(data, mid)
        return f"{data['title']} was updated!", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return f"{mid} movie was deleted!", 204
