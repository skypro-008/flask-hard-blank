import logging

import jwt
from flask import request, abort

from config import Config

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
            jwt.decode(token, Config.JWT_SECRET, algorithms=Config.JWT_ALGO)
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
            user_data = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
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
