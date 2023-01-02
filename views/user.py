import logging

from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
#
from helpers.implemented import user_service
#
from my_exceptions.some_exception import SomeError

#
user_ns = Namespace("users")
#
logger = logging.getLogger("user")

#
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    """
    View class for users
    route '/users/'
    methods GET, POST
    """
    def get(self):
        """
        view all users
        """
        try:
            users = users_schema.dump(
                user_service.get_all()
            )

            return users, 200
        except SomeError as e:
            logger.error(e)

            return [], 500

    def post(self):
        """
        view add new user
        """
        try:
            data = request.json
            new_user = user_service.create(data)
            logger.info(f"User {new_user.username} was added!")

            return (
                f"User {new_user.username} was added!",
                201,
                {"location": f"/users/{new_user.id}"}
            )
        except SomeError as e:
            logger.error(e)

            return {}, 500


@user_ns.route('/<int:uid>')
class UserView(Resource):
    """
    View class for users
    route '/users/{user_id}'
    methods GET, PUT, PATCH, DELETE
    """

    def get(self, uid):
        """
        view single user by user ID
        """
        try:
            # serialized single user by user ID
            user = user_schema.dump(user_service.get_one(uid))

            return user, 200
        except SomeError as e:
            logger.error(e)

            return {}, 404

    def put(self, uid):
        """
        view update user by user ID
        """
        try:
            # json data for updating
            data = request.json
            # update
            user_service.update(data, uid)
            # log info
            logger.info(f"User by id {uid} was updated!")

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404

    def patch(self, uid):
        """
        view partial update user by user ID
        """
        try:
            # json data for partial updating
            data = request.json
            # update
            user_service.update(data, uid)
            # log info
            logger.info(f"User by id {uid} was partial updated!")

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404

    def delete(self, uid):
        """
        view delete user by user ID
        """
        try:
            # delete
            deleted_user = user_service.delete(uid)
            # log info
            logger.info(f"user {deleted_user.username} was deleted!")

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404
