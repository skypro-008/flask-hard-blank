from dao.director import DirectorDAO
from dao.model.director import DirectorSchema


class DirectorService:
    """
    Service for communication between the view and the database handler
    """

    def __init__(self, dao: DirectorDAO):
        """
        Init dao
        """
        self.dao = dao

    def get_all(self):
        """
        Get all directors, serializes them and returns to the view
        """
        # get directors from dao
        directors = self.dao.get_all()
        # serialize to json
        serialize_directors = DirectorSchema().dump(directors, many=True)
        return serialize_directors

    def get_one(self, did):
        """
        Get single director, serializes it and returns to the view
        """
        # get director from dao by director ID
        director = self.dao.get_one(did)
        # serialize to json
        serialize_director = DirectorSchema().dump(director)
        return serialize_director

    def create(self, data):
        """
        uploads new director into database and returns its id
        """
        added_director = self.dao.create(data)[0].id
        return added_director

    def update(self, data, did):
        """
        updates director by director ID
        """
        self.dao.update(data, did)

    def delete(self, did):
        """
        delete director by director ID
        """
        self.dao.delete(did)
