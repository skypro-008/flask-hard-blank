from dao.model.director import Director
from my_exceptions.some_exception import SomeError


class DirectorDAO:
    """
    database manager
    """

    def __init__(self, session):
        """
        session init
        """
        self.session = session

    def get_all(self):
        """
        get all director from db by filters
        """
        try:
            # all directors from database
            directors = self.session.query(Director).all()

            return directors
        except Exception as e:

            raise SomeError(e)

    def get_by_filters(self, page, items_per_page):
        directors = self.session.query(Director).limit(items_per_page * page).offset((page - 1) * items_per_page).all()
        return directors

    def get_one(self, gid):
        """
        get single director by director ID
        """
        # single director
        director = self.session.query(Director).filter(Director.id == gid).first()
        if not director:
            raise SomeError(f"Director with ID {gid} not found")

        return director

    def create(self, data):
        """
        upload new director into database
        """
        try:
            with self.session.begin():
                # upload
                new_director = Director(**data)
                # return data last added director
                self.session.add(new_director)

            return new_director
        except Exception as e:

            raise SomeError(e)

    def update(self, data, gid):
        """
        update director data by director ID
        """
        with self.session.begin():
            # updating
            is_update = self.session.query(Director).filter(Director.id == gid).update(data)
            if not is_update:
                raise SomeError(f"director with ID {gid} not found")

    def delete(self, gid):
        """
        delete director from database bu director ID
        """
        with self.session.begin():
            # deleting
            is_delete = self.session.query(Director).filter(Director.id == gid).delete()
            if not is_delete:
                raise SomeError(f"Director with ID {gid} not found")
