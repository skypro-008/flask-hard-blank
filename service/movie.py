import config
from dao.movie import MovieDAO
from dao.model import MovieSchema


class MovieService:
    """
    Service for communication between the view and the database handler
    """
    def __init__(self, dao: MovieDAO):
        """
        Init dao
        """
        self.dao = dao

    # @staticmethod
    # def get_sorted(movies):
    #     movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    #     return movies

    def get_all_or_by_filters(self, query_params):
        """
        Get all movies, serializes them and returns to the view
        """
        page = int(query_params.get("page", 0))
        status = query_params.get("status", None)
        filters = {key: value for key, value in query_params.items() if
                   value is not None and key not in ('page', 'status')}

        if filters or page:
            # get filtered movies from dao
            items_per_page = config.Config.ITEMS_PER_PAGE
            movies = self.dao.get_by_filters(filters, page, items_per_page, status)
        else:
            # get all movies
            movies = self.dao.get_all(status)
        return movies

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
