from flask import request
from flask_restx import Resource, Namespace

from setup_db import db
from dao.director import DirectorDAO
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_dao = DirectorDAO(db.session)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_dao.get_all()
        directors_serialize = DirectorSchema().dump(directors, many=True)
        return directors_serialize, 200

    def post(self):
        data = request.json
        director_dao.create(data)
        return "added!", 201


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        directors = director_dao.get_one(gid)
        directors_serialize = DirectorSchema().dump(directors)
        return directors_serialize, 200

    def put(self, gid):
        data = request.json
        director_dao.update(data, gid)
        return "updated!", 204

    def patch(self, gid):
        data = request.json
        director_dao.update(data, gid)
        return "partial updated!", 204

    def delete(self, gid):
        director_dao.delete(gid)
        return "deleted", 204
