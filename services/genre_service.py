from repositories.genre_repository import genre_repository as default_genre_repository
from flask import session, abort

class genreService:
    def __init__(self, genre_repository=default_genre_repository):
      self._genre_repository = genre_repository

    def get_genres(self):
      return self._genre_repository.get_genres()

    def get_genres_of_book(self, genres):
      return self._genre_repository.get_genres_of_book(genres)
    
    def add_genre(self,genre, csrf_token):
      if session['admin'] != 1:
        raise Exception('Sinulla ei ole oikeutta tähän toimintoon')
      if session["csrf_token"] != csrf_token:
        abort(403)
      if self._genre_repository.get_genre(genre):
        raise Exception('Sellainen genre on jo olemassa')

      return self._genre_repository.add_genre(genre)      


genre_service = genreService()