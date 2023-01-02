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

    def get_all_or_by_filters(self, filters):
        """
        Get all movies, serializes them and returns to the view
        """
        if filters:
            # get filtered movies from dao
            filtered_movies = self.dao.get_by_filters(filters)

            return filtered_movies

        # get all movies
        return self.dao.get_all()

    def get_one(self, mid):
        """
        Get single movie, serializes it and returns to the view
        """
        # get movie from dao by movie ID
        movie = self.dao.get_one(mid)

        return movie

    def create(self, data):
        """
        uploads new movie into database and returns its id
        """
        new_movie = self.dao.create(data)

        return new_movie

    def update(self, data, mid):
        """
        updates movie by movie ID
        """
        self.dao.update(data, mid)

    def delete(self, mid):
        """
        delete movie by movie ID
        """
        return self.dao.delete(mid)
