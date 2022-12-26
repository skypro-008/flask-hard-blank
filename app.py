
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from setup_db import db
from config import Config
from logger import create_logger

from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    Migrate(app=app, db=db, render_as_batch=True)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    db.init_app(app)
    create_logger(app, 'movie')
    create_logger(app, 'genre')
    create_logger(app, 'director')


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=8888, debug=True)
