import logging

import jwt
from flask import request, abort
# import secret and algorithm
from helpers.constants import JWT_SECRET, JWT_ALGO

logger = logging.getLogger("user")


def auth_required(func):
    """
    Decorator authorization
    """
    def wrapper(*args, **kwargs):
        # data from headers
        data = request.headers

        if "Authorization" not in data:
            abort(401)
        # token extract
        token = data.environ.get("HTTP_AUTHORIZATION").replace("Bearer ", '')
        try:
            # user data from token
            jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGO)
        except Exception as e:
            logger.info(e)
            abort(401)
        else:

            return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
    Decorator permission
    """
    def wrapper(*args, **kwargs):
        # data from headers
        data = request.headers

        if "Authorization" not in data:
            abort(401)
        # token extract
        token = data.environ.get("HTTP_AUTHORIZATION").replace("Bearer ", '')
        try:
            # user data from token
            user_data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            logger.info(e)
            abort(401)
        else:
            # checking user role
            role = user_data.get("role")
            if role != "admin":
                abort(403)

            return func(*args, **kwargs)

    return wrapper
