import logging

from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from helpers.decorators import auth_required
# import configured service object
from implemented import user_service
# import custom error
from my_exceptions.some_exception import SomeError

# create namespace
user_ns = Namespace("user")
# connection logger
logger = logging.getLogger("user")

# schema
user_schema = UserSchema()

#
# @user_ns.route('/')
# class UsersView(Resource):
#     """
#     View class for users
#     route '/users/'
#     methods GET, POST
#     """
#
#     @auth_required
#     def get(self):
#         """
#         view all users
#         """
#         try:
#             query_params = request.args
#             # serialized all or filtered users
#             users = users_schema.dump(
#                 user_service.get_all_or_by_filters(query_params)
#             )
#
#             return users, 200
#         except SomeError as e:
#             logger.error(e)
#
#             return [], 500


@user_ns.route('/')
class UserView(Resource):
    """
    View class user
    route '/user/'
    methods GET, PATCH
    """

    @auth_required
    def get(self):
        """
        view single user
        """
        try:
            data = request.json

            # serialized single user by user ID
            user = user_schema.dump(user_service.get_user_data(data))

            return user, 200
        except SomeError as e:
            logger.error(e)

            return {}, 404

    @auth_required
    def patch(self):
        """
        view update user
        """
        try:
            # json data for partial updating
            data = request.json
            # update
            user_service.update(data)
            # log info
            logger.info(f"User by {data.get('email')} was updated!")

            return {}, 204
        except SomeError as e:
            logger.error(e)

            return {}, 404
    #
    # @auth_required
    # def delete(self, uid):
    #     """
    #     view delete user by user ID
    #     """
    #     try:
    #         # delete
    #         deleted_user = user_service.delete(uid)
    #         # log info
    #         logger.info(f"user {deleted_user.name} was deleted!")
    #
    #         return {}, 204
    #     except SomeError as e:
    #         logger.error(e)
    #
    #         return {}, 404


@user_ns.route("/password/")
class PasswordChangeView(Resource):
    """
    View class set new password
    """
    @auth_required
    def put(self):
        data = request.json

        try:
            user_service.update_password(data)

            return {}, 201

        except Exception:
            return "incorrect password", 400
