import calendar
import datetime

import jwt
from flask import abort

from config import Config
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
        self.JWT_ALGO = Config.JWT_ALGO
        self.JWT_SECRET = Config.JWT_SECRET

    def generate_tokens(self, email, password, is_refresh=False):
        """
        Generate tokens
        """
        # user data from db by email
        user = self.user_service.get_by_email(email)

        # if user not found
        if not user:
            abort(404)

        if not is_refresh:
            # password validation
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        user_data = {
            "email": email,
            "password": password,
            "name": user.name
        }

        # create 30-min tokens
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        user_data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(user_data, self.JWT_SECRET, algorithm=self.JWT_ALGO)

        # create 10-days token
        days10 = datetime.datetime.utcnow() + datetime.timedelta(days=10)
        user_data["exp"] = calendar.timegm(days10.timetuple())
        refresh_token = jwt.encode(user_data, self.JWT_SECRET, algorithm=self.JWT_ALGO)

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
        user = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGO])
        # username form data
        email = user.get("email")

        # generate new tokens
        return self.generate_tokens(email, None, is_refresh=True)


