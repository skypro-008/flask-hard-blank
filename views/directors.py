import logging

from flask import request
from flask_restx import Resource, Namespace

# import configured service object
from implemented import director_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
director_ns = Namespace('directors')
# connection logger
logger = logging.getLogger('director')


@director_ns.route('/')
class DirectorsView(Resource):
    """
    View class for directors
    route '/directors/'
    methods GET, POST
    """

    def get(self):
        """
        view all directors
        """
        try:
            # serialized directors json data
            directors = director_service.get_all()
            return directors, 200
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def post(self):
        """
        view add new director
        """
        try:
            # new director json data
            data = request.json
            # uploads director and returns its ID
            added_director_id = director_service.create(data)
            # log info
            logger.info(f"{data.get('name')} was added!")
            return f"{data.get('name')} was added!", 201, {'location': f'/directors/{added_director_id}'}
        except SomeError as e:
            logger.error(e)
            return {}, 400


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    """
    View class for directors
    route '/directors/{director_id}'
    methods GET, PUT, PATCH, DELETE
    """

    def get(self, gid):
        """
        view single director by director ID
        """
        try:
            # single director
            director = director_service.get_one(gid)
            return director, 200
        except SomeError as e:
            logger.error(e)
            return {}, 400

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
            logger.info(f"{gid} was updated!")
            return "updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400

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
            logger.info(f"{gid} was partial updated!")
            return "partial updated!", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400

    def delete(self, gid):
        """
        view delete director by director ID
        """
        try:
            # delete
            director_service.delete(gid)
            # log info
            logger.info(f"{gid} was delete!")
            return "deleted", 204
        except SomeError as e:
            logger.error(e)
            return {}, 400
