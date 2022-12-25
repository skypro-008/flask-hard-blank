from dao.model.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def _query(self):
        query = self.session.query(Director)

        return query

    def get_all(self):
        directors = self._query().all()

        return directors

    def get_one(self, did):
        director = self._query().filter(Director.id == did).one()

        return director

    def create(self, data):
        self.session.add(Director(**data))
        self.session.commit()

    def update(self, data, did):
        with self.session.begin():
            self.session.query(Director).filter(Director.id == did).update(data)

    def delete(self, did):
        with self.session.begin():
            self.session.query(Director).filter(Director.id == did).delete()
