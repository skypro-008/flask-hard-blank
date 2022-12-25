from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    # def post(self):
    #     return "", 201


@director_ns.route('/<int:did>')
class BookView(Resource):
    def get(self, did):
        return "", 200

    # def put(self, did):
    #     return "", 204
    #
    # def patch(self, did):
    #     return "", 204
    #
    # def delete(self, did):
    #     return "", 204
