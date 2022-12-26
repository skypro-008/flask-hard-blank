import logging

from flask import request
from flask_restx import Resource, Namespace

# import configured service object
from implemented import movie_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
movie_ns = Namespace('movies')
# connection logger
logger = logging.getLogger('movie')


@movie_ns.route('/')
class MoviesView(Resource):
    """
    View class for movies
    route '/movies/'
    methods GET, POST
    """

    def get(self):
        """
        view all movies
        """
        try:
            # filters from request parameters
            filters = request.args
            # filtered and serialized movies json data
            movies = movie_service.get_all(filters)
            return movies, 200
        except SomeError as e:
            logger.error(e)
            return {}, 500

    def post(self):
        """
        view add new movie
        """
        try:
            # new movie json data
            data = request.json
            # uploads movie and returns its ID
            added_movie_id = movie_service.create(data)
            # log info
            logger.info(f"Movie {data.get('title')} was added!")
            return f"Movie {data.get('title')} was added!", 201, {'location': f'/movies/{added_movie_id}'}
        except SomeError as e:
            logger.error(e)
            return {}, 500


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    View class for movies
    route '/movies/{movie_id}'
    methods GET, PUT, PATCH, DELETE
    """

    def get(self, mid):
        """
        view single movie by movie ID
        """
        try:
            # single movie by movie ID
            movie = movie_service.get_one(mid)
            return movie, 200
        except SomeError as e:
            logger.error(e)
            return {}, 404

    def put(self, mid):
        """
        view update movie by movie ID
        """
        try:
            # json data for updating
            data = request.json
            # update
            movie_service.update(data, mid)
            # log info
            logger.info(f"Movie by id {mid} was updated!")
            return f"Movie by id {data['title']} was updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 404

    def patch(self, mid):
        """
        view partial update movie by movie ID
        """
        try:
            # json data for partial updating
            data = request.json
            # update
            movie_service.update(data, mid)
            # log info
            logger.info(f"Movie by id {mid} was partial updated!")
            return f"Movie by id {data['title']} was updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 404

    def delete(self, mid):
        """
        view delete movie by movie ID
        """
        try:
            # delete
            movie_service.delete(mid)
            # log info
            logger.info(f"Movie by id {mid} was deleted!")
            return f"Movie by id {mid} was deleted!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 404
