from dao.model.genre import Genre
from my_exceptions.some_exception import SomeError


class GenreDAO:
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
        get all genre from db by filters
        """
        try:
            # all genres from database
            genres = self.session.query(Genre).all()

            return genres
        except Exception as e:

            raise SomeError(e)

    def get_one(self, gid):
        """
        get single genre by genre ID
        """
        # single genre
        genre = self.session.query(Genre).filter(Genre.id == gid).first()
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
                new_genre = Genre(**data)
                # return data last added genre
                self.session.add(new_genre)

            return new_genre
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
