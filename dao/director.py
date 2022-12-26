from dao.model.director import Director


class DirectorDAO:
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
        query = self.session.query(Director)

        return query

    def get_all(self):
        """
        get all director from db by filters
        """
        # all directors from database
        directors = self._query().all()

        return directors

    def get_one(self, did):
        """
        get single director by director ID
        """
        # single director
        director = self._query().filter(Director.id == did).one()

        return director

    def create(self, data):
        """
        upload new director into database
        """
        with self.session.begin():
            # upload
            self.session.add(Director(**data))
            # return data last added director
            last = self._query().order_by(Director.id.desc()).limit(1).all()
        return last

    def update(self, data, did):
        """
        update director data by director ID
        """
        with self.session.begin():
            # updating
            self.session.query(Director).filter(Director.id == did).update(data)

    def delete(self, did):
        """
        delete director from database bu director ID
        """
        with self.session.begin():
            # deleting
            self.session.query(Director).filter(Director.id == did).delete()
