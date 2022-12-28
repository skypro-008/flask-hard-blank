import logging

from dao.model.movie import Movie
from my_exceptions.some_exception import SomeError


logger = logging.getLogger('movie')


class MovieDAO:
    """
    database manager
    """

    def __init__(self, session):
        """
        session init
        """
        self.session = session

    def get_all(self):
        """
        get all movie from db by filters
        """
        try:
            # raw query to the database
            movies = self.session.query(Movie).all()

            return movies
        except Exception as e:

            raise SomeError(e)

    def get_by_filters(self, filters):
        try:
            # filtered data from database
            movies_query = self.session.query(Movie).filter_by(
                **{key: value for key, value in filters.items() if value is not None}
            )

            movies = movies_query.all()

            return movies
        except Exception as e:

            raise SomeError(e)

    def get_one(self, mid):
        """
        get single movie by movie ID
        """
        # single movie
        movie = self.session.filter(Movie.id == mid).first()
        if not movie:
            raise SomeError(f"Movie with ID {mid} not found")

        return movie

    def create(self, data):
        """
        upload new movie into database
        """
        try:
            with self.session.begin():
                # upload
                self.session.add(Movie(**data))
                # return data last added movie
                last = self.session.order_by(Movie.id.desc()).limit(1).all()

            return last
        except Exception as e:

            raise SomeError(e)

    def update(self, data, mid):
        """
        update movie data by movie ID
        """
        with self.session.begin():
            # updating
            is_update = self.session.query(Movie).filter(Movie.id == mid).update(data)
            if not is_update:
                raise SomeError(f"Movie with ID {mid} not found")

    def delete(self, mid):
        """
        delete movie from database bu movie ID
        """
        with self.session.begin():
            # deleting
            is_delete = self.session.query(Movie).filter(Movie.id == mid).delete()
            if not is_delete:
                raise SomeError(f"Movie with ID {mid} not found")
