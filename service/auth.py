import calendar
import datetime

import jwt
from flask import abort

from helpers.constants import JWT_ALGO, JWT_SECRET
from service.user import UserService


class AuthService:
    """
    Service for communication between the view and the database handler
    """
    def __init__(self, user_service: UserService):
        """
        Init service
        """
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        """
        Generate tokens
        """
        # user data from db by username
        user = self.user_service.get_by_username(username)

        # if user not found
        if not user:
            abort(404)

        if not is_refresh:
            # password validation
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        user_data = {
            "username": username,
            "password": password,
            "role": user.role
        }

        # create 30-min tokens
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        user_data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(user_data, JWT_SECRET, algorithm=JWT_ALGO)

        # create 10-days token
        days10 = datetime.datetime.utcnow() + datetime.timedelta(days=10)
        user_data["exp"] = calendar.timegm(days10.timetuple())
        refresh_token = jwt.encode(user_data, JWT_SECRET, algorithm=JWT_ALGO)

        # return created tokens
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, token):
        """
        Refresh tokens
        """
        # decode data from tokens
        user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        # username form data
        username = user.get("username")

        # generate new tokens
        return self.generate_tokens(username, None, is_refresh=True)


