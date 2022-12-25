from flask_restx import Resource, Namespace

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import MovieSchema, Movie
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class BooksView(Resource):
    def get(self):
        movies = db.session.query(Movie.id, Movie.title, Movie.rating, Movie.year, Movie.description, Movie.trailer,
                                  Director.name.label('director'), Genre.name.label('genre')) \
            .join(Director, Director.id == Movie.director_id) \
            .join(Genre, Genre.id == Movie.genre_id).all()
        se_m = MovieSchema().dump(movies, many=True)
        return se_m, 200

    def post(self):
        return "", 201


@movie_ns.route('/<int:mid>')
class BookView(Resource):
    def get(self, mid):
        return "", 200

    def put(self, mid):
        return "", 204

    def patch(self, mid):
        return "", 204

    def delete(self, mid):
        return "", 204
