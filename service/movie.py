from dao.movie import MovieDAO
from dao.model.movie import MovieSchema


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        movies = self.dao.get_all(filters)
        serialize_movies = MovieSchema().dump(movies, many=True)
        return serialize_movies

    def get_one(self, mid):
        movie = self.dao.get_one(mid)
        serialize_movie = MovieSchema().dump(movie)
        return serialize_movie

    def create(self, data):
        added_movie = self.dao.create(data)[0].id
        return added_movie

    def update(self, data, mid):
        self.dao.update(data, mid)

    def delete(self, mid):
        self.dao.delete(mid)
