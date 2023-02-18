from dao.model.user import User
from my_exceptions.some_exception import SomeError


class UserDAO:
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
        get all users from db by filters
        """
        try:
            # all users from database
            users = self.session.query(User.id, User.name, User.email).all()

            return users
        except Exception as e:
            raise SomeError(e)

    def get_user_by_email(self, email):
        """
        get user from db by email
        """
        try:
            user = self.session.query(User).filter(User.email == email).first()

            return user
        except Exception as e:
            raise SomeError(e)

    def get_by_filters(self, page, items_per_page):
        """
        get filtered users
        """
        users = self.session.query(User.id, User.name, User.email).limit(items_per_page * page).offset(
            (page - 1) * items_per_page).all()
        return users

    def get_one(self, uid):
        """
        get single user by user ID
        """
        # single user
        user = self.session.query(User.id, User.name, User.email).filter(User.id == uid).first()
        if not user:
            raise SomeError(f"User with ID {uid} not found")

        return user

    def get_by_email(self, email):
        """
        get single user by username
        """
        # user by username
        user = self.session.query(User).filter(User.email == email).first()
        if not user:
            raise SomeError(f"User {email} not found")

        return user

    def create(self, data):
        """
        upload new user into database
        """
        try:
            with self.session.begin():
                # upload
                new_user = User(**data)
                # return data last added user
                self.session.add(new_user)

            return new_user
        except Exception as e:
            raise SomeError(e)

    def update(self, data, email):
        """
        update user data by user ID
        """
        with self.session.begin():
            # updating
            is_update = self.session.query(User).filter(User.email == email).update(data)
            if not is_update:
                raise SomeError(f"User with {email} not found")

    def password_update(self, email, password):
        """
        set new password
        """
        user = self.session.query(User).filter(User.email == email).first()
        user.password = password
        self.session.commit()

    def delete(self, uid):
        """
        delete user from database bu user ID
        """
        with self.session.begin():
            user_query = self.session.query(User).filter(User.id == uid)
            user_for_return = user_query.first()
            # deleting
            is_deleted = user_query.delete()
            if not is_deleted:
                raise SomeError(f"User with ID {uid} not found")

            return user_for_return
