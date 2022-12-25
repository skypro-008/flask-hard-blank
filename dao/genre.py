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
        with self.session.begin():
            self.session.add(Genre(**data))
            last = self._query().order_by(Genre.id.desc()).limit(1).all()
        return last

    def update(self, data, gid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == gid).update(data)

    def delete(self, gid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == gid).delete()
