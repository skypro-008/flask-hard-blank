from dao.director import DirectorDAO


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

        return directors

    def get_one(self, did):
        """
        Get single director, serializes it and returns to the view
        """
        # get director from dao by director ID
        director = self.dao.get_one(did)

        return director

    def create(self, data):
        """
        uploads new director into database and returns its id
        """
        new_director = self.dao.create(data)

        return new_director

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
