import base64
import hashlib
import hmac

import jwt

import config
from dao.user import UserDAO


class UserService:
    """
    Service for communication between the view and the database handler
    """

    def __init__(self, dao: UserDAO):
        """
        Init dao
        """
        self.dao = dao
        self.PWD_HASH_ITERATIONS = config.Config.PWD_HASH_ITERATIONS
        self.PWD_HASH_SALT = config.Config.PWD_HASH_SALT

    def get_all_or_by_filters(self, query_params):
        """
        Get all users
        """
        page = int(query_params.get("page", 0))
        if page:
            items_per_page = config.Config.ITEMS_PER_PAGE
            users = self.dao.get_by_filters(page, items_per_page)
        else:
            # get filtered users from dao
            users = self.dao.get_all()

        return users

    def get_user_data(self, data):
        """
        get user data
        """
        user_data = self.get_data_from_tokens(data)
        user = self.dao.get_user_by_email(user_data.get("email"))
        user.password = "*" * len(user_data.get("password"))
        return user

    def get_data_from_tokens(self, data):
        """
        return data extract from token
        """
        refresh_token = data.get("refresh_token")

        data = jwt.decode(refresh_token, config.Config.JWT_SECRET, algorithms=[config.Config.JWT_ALGO])

        return data

    def get_one(self, uid):
        """
        Get single user
        """
        # get user from dao by user ID
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        """
        Get single user
        """
        return self.dao.get_by_email(email)

    def create(self, data):
        """
        uploads new user into database and returns its id
        """
        # converting a normal password to hash
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        """
        updates user by email
        """
        email = self.get_data_from_tokens(data).get("email")
        data.pop("refresh_token")
        return self.dao.update(data, email)

    def update_password(self, data):
        """
        set new password
        """
        user_data = self.get_data_from_tokens(data)
        email = user_data.get("email")
        hash_password_1 = self.get_hash(data.get("password_1"))
        hash_password_2 = self.get_hash(data.get("password_2"))
        if hash_password_1 == self.dao.get_user_by_email(email).password:
            # password = {
            #     "password": hash_password_2
            # }
            self.dao.password_update(email, hash_password_2)
        else:
            raise Exception

    def delete(self, uid):
        """
        delete user by user ID
        """
        return self.dao.delete(uid)

    def get_hash(self, password):
        """
        converting a normal password to hash
        """
        # hash function sha256
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            self.PWD_HASH_SALT,
            self.PWD_HASH_ITERATIONS
        )
        # hash password
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password, other_password):
        """
        compare passwords
        """
        # decode password from string
        decode_password = base64.b64decode(password)
        # converting a normal password to hash
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            self.PWD_HASH_SALT,
            self.PWD_HASH_ITERATIONS
        )
        # compare two hash password
        return hmac.compare_digest(decode_password, hash_digest)
