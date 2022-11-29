from repositories.genre_repository import genre_repository as default_genre_repository

class genreService:
    def __init__(self, genre_repository=default_genre_repository):
      self._genre_repository = genre_repository

    def add_genre(self, name):
      if len(name)<3 or len(name)>50:
        raise Exception("Anna genrelle kunnon nimen")
      if name == None:
          raise Exception("jotain meni väärin")

      return self._genre_repository.add_genre(name)

    def get_genres(self):
      return self._genre_repository.get_genres()

    def get_genres_of_book(self, genres):
      return self._genre_repository.get_genres_of_book(genres)


    def delete_genre(self, genre_id):
      return self._genre_repository.hide_genre(genre_id)


genre_service = genreService()