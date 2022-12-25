from setup_db import db

from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.director import DirectorDAO

from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
