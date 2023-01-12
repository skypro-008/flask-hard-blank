import logging

from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
# import decorators
from helpers.decorators import auth_required, admin_required
# import configured service object
from implemented import director_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
director_ns = Namespace('directors')
# connection logger
logger = logging.getLogger('director')
# schemas
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    """
    View class for directors
    route '/directors/'
    methods GET, POST
    """
    @auth_required
    def get(self):
        """
        view all directors
        """
        try:
            query_params = request.args
            # serialized directors json data
            directors = directors_schema.dump(director_service.get_all_or_by_filters(query_params))

            return directors, 200
        except SomeError as e:
            logger.error(e)

            return {}, 500

    @auth_required
    # @admin_required
    def post(self):
        """
        view add new director
        """
        try:
            # new director json data
            data = request.json
            # uploads director and returns its ID
            new_director = director_service.create(data)
            # log info
            logger.info(f"Director {new_director.name} was added!")

            return (
                f"Director {new_director.name} was added!",
                201,
                {'location': f'/directors/{new_director.id}'}
            )
        except SomeError as e:
            logger.error(e)

            return {}, 500


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    """
    View class for directors
    route '/directors/{director_id}'
    methods GET, PUT, PATCH, DELETE
    """
    @auth_required
    def get(self, gid):
        """
        view single director by director ID
        """
        try:
            # single director
            director = director_schema.dump(director_service.get_one(gid))

            return director, 200
        except SomeError as e:
            logger.error(e)

            return {}, 404

    @auth_required
    # @admin_required
    def put(self, gid):
        """
        view update director by director ID
        """
        try:
            # json data for updating
            data = request.json
            # update
            director_service.update(data, gid)
            # log info
            logger.info(f"Director by id {gid} was updated!")

            return f"Director by id {gid} was updated!", 204
        except SomeError as e:
            logger.error(e)

            return {}, 400

    @auth_required
    # @admin_required
    def patch(self, gid):
        """
        view partial update director by director ID
        """
        try:
            # json data for partial updating
            data = request.json
            # update
            director_service.update(data, gid)
            # log info
            logger.info(f"Director by id {gid} was partial updated!")

            return f"Director by id {gid} was partial updated!", 204
        except SomeError as e:
            logger.error(e)

            return {}, 400

    @auth_required
    # @admin_required
    def delete(self, gid):
        """
        view delete director by director ID
        """
        try:
            # delete
            director_service.delete(gid)
            # log info
            logger.info(f"Director by id {gid} was delete!")

            return f"Director by id {gid} was delete!", 204
        except SomeError as e:
            logger.error(e)

            return {}, 404
