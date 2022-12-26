from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre


class MovieDAO:
    """
    database manager
    """
    def __init__(self, session):
        """
        session init
        """
        self.session = session

    def _query(self):
        """
        query building
        """
        query = self.session.query(
            Movie.id,
            Movie.title,
            Movie.rating,
            Movie.year,
            Movie.description,
            Movie.trailer,
            Director.name.label('director'),
            Genre.name.label('genre')
        ) \
            .join(Director, Director.id == Movie.director_id) \
            .join(Genre, Genre.id == Movie.genre_id)
        return query

    def get_all(self, filters):
        """
        get all movie from db by filters
        """
        # raw query to the database
        movies_query = self._query()
        # applying filters to a query
        if filters.get('director_id') is not None:
            movies_query = movies_query.filter(Movie.director_id == filters.get('director_id'))
        if filters.get('genre_id') is not None:
            movies_query = movies_query.filter(Movie.genre_id == filters.get('genre_id'))
        if filters.get('year') is not None:
            movies_query = movies_query.filter(Movie.year == filters.get('year'))
        # all filtered movie from database
        movies = movies_query.all()

        return movies

    def get_one(self, mid):
        """
        get single movie by movie ID
        """
        # single movie
        movie = self._query().filter(Movie.id == mid).one()

        return movie

    def create(self, data):
        """
        upload new movie into database
        """
        with self.session.begin():
            # upload
            self.session.add(Movie(**data))
            # return data last added movie
            last = self._query().order_by(Movie.id.desc()).limit(1).all()
        return last

    def update(self, data, mid):
        """
        update movie data by movie ID
        """
        with self.session.begin():
            # updating
            self.session.query(Movie).filter(Movie.id == mid).update(data)

    def delete(self, mid):
        """
        delete movie from database bu movie ID
        """
        with self.session.begin():
            # deleting
            self.session.query(Movie).filter(Movie.id == mid).delete()
