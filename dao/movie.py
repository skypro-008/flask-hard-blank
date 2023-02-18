import config
from dao.model.movie import Movie
from my_exceptions.some_exception import SomeError
from sqlalchemy import desc
class MovieDAO:
    """
    database manager
    """

    def __init__(self, session):
        """
        session init
        """
        self.session = session

    def get_all(self, status=None):
        """
        get all movie from db by filters
        """
        try:
            if status:
                movies = self.session.query(Movie).order_by(desc(Movie.year)).all()
            else:
                # raw query to the database
                movies = self.session.query(Movie).all()

            return movies
        except Exception as e:

            raise SomeError(e)

    def get_by_filters(self, filters, page, items_per_page, status=None):
        try:
            if status:
                movies_query = self.session.query(Movie).order_by(desc(Movie.year))
            else:
                movies_query = self.session.query(Movie)
            # filtered data from database
            movies_query = movies_query.filter_by(
                **filters
            ).limit(items_per_page * page).offset((page - 1) * items_per_page).all()
            return movies_query
        except Exception as e:

            raise SomeError(e)

    def get_one(self, mid):
        """
        get single movie by movie ID
        """
        # single movie
        movie = self.session.query(Movie).filter(Movie.id == mid).first()
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
                new_movie = Movie(**data)
                self.session.add(new_movie)
                # return data last added movie
            return new_movie
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
            movie_query = self.session.query(Movie).filter(Movie.id == mid)
            movie_for_return = movie_query.first()
            is_delete = movie_query.delete()
            if not is_delete:
                raise SomeError(f"Movie with id {mid} not found")

            return movie_for_return
