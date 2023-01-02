import os

from helpers.constants import LOG_DIR


class Config:
    SECRET_HERE = '249y823r9v8238r9u'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RESTX_JSON = {"ensure_ascii": False}
    JSON_AS_ASCII = False
    DEBUG = True

    # config log
    USER_LOG_PATH = os.path.join(LOG_DIR, 'user.log')
    MOVIE_LOG_PATH = os.path.join(LOG_DIR, 'movie.log')
    GENRE_LOG_PATH = os.path.join(LOG_DIR, 'genre.log')
    DIRECTOR_LOG_PATH = os.path.join(LOG_DIR, 'director.log')
    LOG_FORMAT = "[%(levelname)s]: [%(name)s] %(asctime)s: " \
                 "Full path to file [%(pathname)s] - function name %(funcName)s(%(lineno)d) - %(message)s"
    DATE_FORMAT = "%d-%m-%y %H:%M:%S"
