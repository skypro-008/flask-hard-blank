from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def _query(self):
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
        movies_query = self._query()
        if filters.get('director_id') is not None:
            movies_query = movies_query.filter(Movie.director_id == filters.get('director_id'))
        if filters.get('genre_id') is not None:
            movies_query = movies_query.filter(Movie.genre_id == filters.get('genre_id'))
        if filters.get('year') is not None:
            movies_query = movies_query.filter(Movie.year == filters.get('year'))

        movie = movies_query.all()

        return movie

    def get_one(self, mid):
        movie = self._query().filter(Movie.id == mid).one()

        return movie

    def create(self, data):
        self.session.add(Movie(**data))
        self.session.commit()

    def update(self, data, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).update(data)

    def delete(self, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).delete()
