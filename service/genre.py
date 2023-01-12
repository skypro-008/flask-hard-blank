import config
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

    def get_all_or_by_filter(self, query_params):
        """
        Get all genres, serializes them and returns to the view
        """
        page = int(query_params.get("page", 0))
        if page:
            items_per_page = config.Config.ITEMS_PER_PAGE
            genres = self.dao.get_by_filters(page, items_per_page)
        # get genres from dao
        else:
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
        new_genre = self.dao.create(data)

        return new_genre

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
