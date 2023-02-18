from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from setup_db import db
from config import Config
from logger import create_logger

from views.auth.auth import auth_ns
from views.auth.user import user_ns
from views.main.movie import movie_ns
from views.main.genre import genre_ns
from views.main.director import director_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    register_extensions(app)
    return app


def register_extensions(app):
    Migrate(app=app, db=db, render_as_batch=True)
    api = Api(
        app,
        version='1.0',
        title='Api cinema project',
        doc='/docs',
        prefix='/api'
    )
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    db.init_app(app)
    create_logger(app, 'user')
    create_logger(app, 'movie')
    create_logger(app, 'genre')
    create_logger(app, 'director')


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=8888, debug=True)
