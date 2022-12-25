from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    # def post(self):
    #     return "", 201


@genre_ns.route('/<int:gid>')
class BookView(Resource):
    def get(self, gid):
        return "", 200

    # def put(self, gid):
    #     return "", 204
    #
    # def patch(self, gid):
    #     return "", 204
    #
    # def delete(self, gid):
    #     return "", 204
