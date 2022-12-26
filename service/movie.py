from dao.movie import MovieDAO
from dao.model.movie import MovieSchema


class MovieService:
    """
    Service for communication between the view and the database handler
    """
    def __init__(self, dao: MovieDAO):
        """
        Init dao
        """
        self.dao = dao

    def get_all(self, filters):
        """
        Get all movies, serializes them and returns to the view
        """
        # get filtered movies from dao
        movies = self.dao.get_all(filters)
        # serialize to json
        serialize_movies = MovieSchema().dump(movies, many=True)
        return serialize_movies

    def get_one(self, mid):
        """
        Get single movie, serializes it and returns to the view
        """
        # get movie from dao by movie ID
        movie = self.dao.get_one(mid)
        # serialize to json
        serialize_movie = MovieSchema().dump(movie)
        return serialize_movie

    def create(self, data):
        """
        uploads new movie into database and returns its id
        """
        added_movie = self.dao.create(data)[0].id
        return added_movie

    def update(self, data, mid):
        """
        updates movie by movie ID
        """
        self.dao.update(data, mid)

    def delete(self, mid):
        """
        delete movie by movie ID
        """
        self.dao.delete(mid)
