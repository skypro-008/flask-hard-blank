from dao.model.user import User
from my_exceptions.some_exception import SomeError


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        try:
            users = self.session.query(User).all()

            return users
        except Exception as e:
            raise SomeError(e)

    def get_one(self, uid):
        user = self.session.query(User).filter(User.id == uid).first()
        if not user:
            raise SomeError(f"User with ID {uid} not found")

        return user

    def create(self, data):
        try:
            with self.session.begin():
                new_user = User(**data)
                self.session.add(new_user)

            return new_user
        except Exception as e:
            raise SomeError(e)

    def update(self, data, uid):

        with self.session.begin():
            is_update = self.session.query(User).filter(User.id == uid).update(data)
            if not is_update:
                raise SomeError(f"User with ID {uid} not found")

    def delete(self, uid):
        with self.session.begin():
            user_query = self.session.query(User).filter(User.id == uid)
            user_for_return = user_query.first()
            is_deleted = user_query.delete()
            if not is_deleted:
                raise SomeError(f"User with ID {uid} not found")

            return user_for_return
