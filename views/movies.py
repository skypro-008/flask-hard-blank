from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201


@movie_ns.route('/<int:mid>')
class BookView(Resource):
    def get(self, mid):
        return "", 200

    def put(self, mid):
        return "", 204

    def patch(self, mid):
        return "", 204

    def delete(self, mid):
        return "", 204
