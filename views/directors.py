from flask import request
from flask_restx import Resource, Namespace

from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors, 200

    def post(self):
        data = request.json
        director_service.create(data)
        added_director_id = director_service.create(data)
        return "added!", 201, {'location': f'/movies/{added_director_id}'}


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        director = director_service.get_one(gid)
        return director, 200

    def put(self, gid):
        data = request.json
        director_service.update(data, gid)
        return "updated!", 204

    def patch(self, gid):
        data = request.json
        director_service.update(data, gid)
        return "partial updated!", 204

    def delete(self, gid):
        director_service.delete(gid)
        return "deleted", 204
