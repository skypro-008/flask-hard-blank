import logging

from flask import request
from flask_restx import Resource, Namespace

# import configured service object
from implemented import genre_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
genre_ns = Namespace('genres')
# connection logger
logger = logging.getLogger('genre')


@genre_ns.route('/')
class GenresView(Resource):
    """
    View class for genres
    route '/genres/'
    methods GET, POST
    """

    def get(self):
        """
        view all genres
        """
        try:
            # serialized genres json data
            genres = genre_service.get_all()
            return genres, 200
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def post(self):
        """
        view add new genre
        """
        try:
            # new genre json data
            data = request.json
            # uploads genre and returns its ID
            added_genre_id = genre_service.create(data)
            # log info
            logger.info(f"{data.get('name')} was added!")
            return f"{data.get('name')} was added!", 201, {'location': f'/genres/{added_genre_id}'}
        except SomeError as e:
            logger.error(e)
            return {}, 400


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    View class for genres
    route '/genres/{genre_id}'
    methods GET, PUT, PATCH, DELETE
    """

    def get(self, gid):
        """
        view single genre by genre ID
        """
        try:
            # single genre
            genre = genre_service.get_one(gid)
            return genre, 200
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def put(self, gid):
        """
        view update genre by genre ID
        """
        try:
            # json data for updating
            data = request.json
            # update
            genre_service.update(data, gid)
            # log info
            logger.info(f"{gid} was updated!")
            return "updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def patch(self, gid):
        """
        view partial update genre by genre ID
        """
        try:
            # json data for partial updating
            data = request.json
            # update
            genre_service.update(data, gid)
            # log info
            logger.info(f"{gid} was partial updated!")
            return "partial updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def delete(self, gid):
        """
        view delete genre by genre ID
        """
        try:
            # delete
            genre_service.delete(gid)
            # log info
            logger.info(f"{gid} was delete!")
            return "deleted", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400
