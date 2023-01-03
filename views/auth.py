from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import auth_service

# namespace
auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    """
    View authorization
    route '/auth/
    methods POST, PUT
    """
    def post(self):
        """
        Authorization user, generate tokens
        """
        # new user data
        user_data = request.json
        username = user_data.get("username")
        password = user_data.get("password")

        if None in [username, password]:
            abort(400)
        # generate tokens for user
        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        """
        Refresh tokens
        """
        user_data = request.json
        token = user_data.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
