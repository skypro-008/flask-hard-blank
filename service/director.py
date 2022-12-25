from dao.director import DirectorDAO
from dao.model.director import DirectorSchema


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        directors = self.dao.get_all()
        serialize_directors = DirectorSchema().dump(directors, many=True)
        return serialize_directors

    def get_one(self, did):
        director = self.dao.get_one(did)
        serialize_director = DirectorSchema().dump(director)
        return serialize_director

    def create(self, data):
        self.dao.create(data)
        added_director_id = self.dao.create(data)[0].id
        return added_director_id

    def update(self, data, did):
        self.dao.update(data, did)

    def delete(self, did):
        self.dao.delete(did)
