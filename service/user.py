import base64
import hashlib
import hmac

from dao.user import UserDAO
from helpers.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT


class UserService:
    """
    Service for communication between the view and the database handler
    """

    def __init__(self, dao: UserDAO):
        """
        Init dao
        """
        self.dao = dao

    def get_all(self):
        """
        Get all users, serializes them and returns to the view
        """
        # get filtered users from dao
        return self.dao.get_all()

    def get_one(self, uid):
        """
        Get single user, serializes it and returns to the view
        """
        # get user from dao by user ID
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        """
        Get single user, serializes it and returns to the view
        """
        return self.dao.get_by_username(username)

    def create(self, data):
        """
        uploads new user into database and returns its id
        """
        # converting a normal password to hash
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data, uid):
        """
        updates user by user ID
        """
        # converting a normal password to hash
        if "password" in data:
            data["password"] = self.get_hash(data["password"])
        return self.dao.update(data, uid)

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
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
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
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        # compare two hash password
        return hmac.compare_digest(decode_password, hash_digest)
