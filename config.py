import os

import dotenv

from helpers.constants import LOG_DIR


class Config:
    dotenv.load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")

    PWD_HASH_SALT = os.environ.get("PWD_HASH_SALT").encode("utf-8")
    PWD_HASH_ITERATIONS = int(os.environ.get("PWD_HASH_ITERATIONS"))

    JWT_ALGO = os.environ.get("JWT_ALGO")
    JWT_SECRET = os.environ.get("JWT_SECRET")

    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RESTX_JSON = {"ensure_ascii": False}
    JSON_AS_ASCII = False
    DEBUG = True

    # paginate
    ITEMS_PER_PAGE = 12

    # configure log
    USER_LOG_PATH = os.path.join(LOG_DIR, 'user.log')
    MOVIE_LOG_PATH = os.path.join(LOG_DIR, 'movie.log')
    GENRE_LOG_PATH = os.path.join(LOG_DIR, 'genre.log')
    DIRECTOR_LOG_PATH = os.path.join(LOG_DIR, 'director.log')
    LOG_FORMAT = "[%(levelname)s]: [%(name)s] %(asctime)s: " \
                 "Full path to file [%(pathname)s] - function name %(funcName)s(%(lineno)d) - %(message)s"
    DATE_FORMAT = "%d-%m-%y %H:%M:%S"
