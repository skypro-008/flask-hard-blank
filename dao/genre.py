from dao.model.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def _query(self):
        query = self.session.query(Genre)

        return query

    def get_all(self):
        genres = self._query().all()

        return genres

    def get_one(self, gid):
        genre = self._query().filter(Genre.id == gid).one()

        return genre

    def create(self, data):
        self.session.add(Genre(**data))
        self.session.commit()

    def update(self, data, gid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == gid).update(data)

    def delete(self, gid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == gid).delete()
