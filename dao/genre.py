from dao.model.genre import Genre


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
        # all genres from database
        genres = self._query().all()

        return genres

    def get_one(self, gid):
        """
        get single genre by genre ID
        """
        # single genre
        genre = self._query().filter(Genre.id == gid).one()

        return genre

    def create(self, data):
        """
        upload new genre into database
        """
        with self.session.begin():
            # upload
            self.session.add(Genre(**data))
            # return data last added genre
            last = self._query().order_by(Genre.id.desc()).limit(1).all()
        return last

    def update(self, data, gid):
        """
        update genre data by genre ID
        """
        with self.session.begin():
            # updating
            self.session.query(Genre).filter(Genre.id == gid).update(data)

    def delete(self, gid):
        """
        delete genre from database bu genre ID
        """
        with self.session.begin():
            # deleting
            self.session.query(Genre).filter(Genre.id == gid).delete()
