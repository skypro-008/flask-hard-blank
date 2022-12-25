
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from config import Config
from setup_db import db

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


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=8888, debug=True)
