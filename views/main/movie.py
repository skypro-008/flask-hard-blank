import logging

from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
# import decorators
from helpers.decorators import auth_required, admin_required
# import configured service object
from implemented import movie_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
movie_ns = Namespace('movies')
# connection logger
logger = logging.getLogger('movie')

# schemas
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    View class for movies
    route '/movies/'
    methods GET, POST
    """

    @auth_required
    def get(self):
        """
        view all movies
        """
        try:
            # filters from request parameters
            query_params = request.args
            # serialized all or filtered movies
            movies = movies_schema.dump(
                movie_service.get_all_or_by_filters(query_params)
            )

            return movies, 200
        except SomeError as e:
            logger.error(e)

            return [], 500

    @auth_required
    # @admin_required
    def post(self):
        """
        view add new movie
        """
        try:
            # new movie json data
            data = request.json
            # uploads movie and returns its ID
            new_movie = movie_service.create(data)
            # log info
            logger.info(f"Movie {new_movie.title} was added!")

            return (
                f"Movie {new_movie.title} was added!",
                201,
                {"location": f"/movies/{new_movie.id}"}
            )
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

    @auth_required
    def get(self, mid):
        """
        view single movie by movie ID
        """
        try:
            # serialized single movie by movie ID
            movie = movie_schema.dump(movie_service.get_one(mid))

            return movie, 200
        except SomeError as e:
            logger.error(e)

            return {}, 404

    @admin_required
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

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404

    @auth_required
    # @admin_required
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

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404

    @auth_required
    # @admin_required
    def delete(self, mid):
        """
        view delete movie by movie ID
        """
        try:
            # delete
            deleted_movie = movie_service.delete(mid)
            # log info
            logger.info(f"Movie {deleted_movie.title} was deleted!")

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404
