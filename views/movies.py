from flask import request
from flask_restx import Resource, Namespace

from setup_db import db
from dao.movie import MovieDAO
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_dao = MovieDAO(db.session)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters = request.args
        movies = movie_dao.get_all(filters)
        movies_serialize = MovieSchema().dump(movies, many=True)
        return movies_serialize, 200

    def post(self):
        data = request.json
        movie_dao.create(data)
        return f"{data.get('title')} was added!", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie_q = movie_dao.get_one(mid)
        movie = MovieSchema().dump(movie_q)
        return movie, 200

    def put(self, mid):
        data = request.json
        movie_dao.update(data, mid)
        return f"{data['title']} was updated!", 204

    def patch(self, mid):
        data = request.json
        movie_dao.update(data, mid)
        return f"{data['title']} was updated!", 204

    def delete(self, mid):
        movie_dao.delete(mid)
        return f"{mid} movie was deleted!", 204
