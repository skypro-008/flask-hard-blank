from dao.genre import GenreDAO
from dao.model.genre import GenreSchema


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        genres = self.dao.get_all()
        serialize_genres = GenreSchema().dump(genres, many=True)
        return serialize_genres

    def get_one(self, gid):
        genre = self.dao.get_one(gid)
        serialize_genre = GenreSchema().dump(genre)
        return serialize_genre

    def create(self, data):
        self.dao.create(data)
        added_genre_id = self.dao.create(data)[0].id
        return added_genre_id

    def update(self, data, gid):
        self.dao.update(data, gid)

    def delete(self, gid):
        self.dao.delete(gid)
