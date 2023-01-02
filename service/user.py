import base64
import hashlib

from dao.user import UserDAO
from helpers.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data, uid):
        data["password"] = self.get_hash(data["password"])
        return self.dao.update(data, uid)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)
