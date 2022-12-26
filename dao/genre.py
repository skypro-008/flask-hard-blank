import logging

from dao.model.genre import Genre
from my_exceptions.some_exception import SomeError

logger = logging.getLogger('genre')


class GenreDAO:
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
        query = self.session.query(Genre)

        return query

    def get_all(self):
        """
        get all genre from db by filters
        """
        try:
            # all genres from database
            genres = self._query().all()
            return genres
        except Exception as e:
            raise SomeError(e)

    def get_one(self, gid):
        """
        get single genre by genre ID
        """
        # single genre
        genre = self._query().filter(Genre.id == gid).first()
        if not genre:
            raise SomeError(f"Genre with ID {gid} not found")
        return genre

    def create(self, data):
        """
        upload new genre into database
        """
        try:
            with self.session.begin():
                # upload
                self.session.add(Genre(**data))
                # return data last added genre
                last = self._query().order_by(Genre.id.desc()).limit(1).all()
            return last
        except Exception as e:
            raise SomeError(e)

    def update(self, data, gid):
        """
        update genre data by genre ID
        """
        with self.session.begin():
            # updating
            is_update = self.session.query(Genre).filter(Genre.id == gid).update(data)
            if not is_update:
                raise SomeError(f"Genre with ID {gid} not found")

    def delete(self, gid):
        """
        delete genre from database bu genre ID
        """
        with self.session.begin():
            # deleting
            is_delete = self.session.query(Genre).filter(Genre.id == gid).delete()
            if not is_delete:
                raise SomeError(f"Genre with ID {gid} not found")
