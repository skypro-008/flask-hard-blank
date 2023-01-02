import logging

from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
# import configured service object
from helpers.implemented import genre_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
genre_ns = Namespace('genres')
# connection logger
logger = logging.getLogger('genre')
# schemas
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


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
            genres = genres_schema.dump(genre_service.get_all())

            return genres, 200
        except SomeError as e:
            logger.error(e)

            return [], 500

    def post(self):
        """
        view add new genre
        """
        try:
            # new genre json data
            data = request.json
            # uploads genre and returns its ID
            new_genre = genre_service.create(data)
            # log info
            logger.info(f"Genre {new_genre.name} was added!")

            return (
                f"Genre {new_genre.name} was added!",
                201,
                {'location': f'/genres/{new_genre.id}'}
            )
        except SomeError as e:
            logger.error(e)

            return {}, 500


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
            # serialized single genre
            genre = genre_schema.dump(genre_service.get_one(gid))

            return genre, 200
        except SomeError as e:
            logger.error(e)

            return {}, 404

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
            logger.info(f"Genre by id {gid} was updated!")

            return f"Genre by id {gid} was updated!", 204
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
            logger.info(f"Genre by id {gid} was partial updated!")

            return f"Genre by id {gid} was partial updated!", 204
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
            logger.info(f"Genre by id {gid} was delete!")

            return f"Genre by id {gid} was delete!", 204
        except SomeError as e:
            logger.error(e)

            return {}, 404
