from dao.genre import GenreDAO


class GenreService:
    """
    Service for communication between the view and the database handler
    """

    def __init__(self, dao: GenreDAO):
        """
        Init dao
        """
        self.dao = dao

    def get_all(self):
        """
        Get all genres, serializes them and returns to the view
        """
        # get genres from dao
        genres = self.dao.get_all()

        return genres

    def get_one(self, gid):
        """
        Get single genre, serializes it and returns to the view
        """
        # get genre from dao by genre ID
        genre = self.dao.get_one(gid)

        return genre

    def create(self, data):
        """
        uploads new genre into database and returns its id
        """
        added_genre = self.dao.create(data)[0].id

        return added_genre

    def update(self, data, gid):
        """
        updates genre by genre ID
        """
        self.dao.update(data, gid)

    def delete(self, gid):
        """
        delete genre by genre ID
        """
        self.dao.delete(gid)
