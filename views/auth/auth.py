import logging

from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import auth_service
from my_exceptions.some_exception import SomeError

# namespace
auth_ns = Namespace('auth')
# create logger
logger = logging.getLogger('user')


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    """
    View authorization
    route '/auth/login/
    methods POST, PUT
    """
    def post(self):
        """
        Authorization user, generate tokens
        """
        # new user data
        user_data = request.json
        email = user_data.get("email")
        password = user_data.get("password")

        if None in [email, password]:
            abort(400)
        # generate tokens for user
        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        """
        Refresh tokens
        """
        user_data = request.headers
        token = user_data.environ.get("HTTP_AUTHORIZATION").replace("Bearer ", '')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        """
        Register new user
        """
        try:
            # new user data
            user_data = request.json
            new_user = auth_service.user_service.create(user_data)

            return (
                f"User {new_user.name} was added!",
                201,
                {"location": f"/api/users/{new_user.id}"}
            )
        except SomeError as e:
            logger.error(e)

            return {}, 500
