from database import database_connection
from entities.genre import Genre

def get_genre_by_row(row):
  return Genre(row['id'], row['name']) if row else None

class GenreRepository:
  def __init__(self, connection):
      self.connection = connection

  def get_genres(self):
    cursor = self.connection.session
    sql = "SELECT id, name FROM genres WHERE visible=1"
    rows = cursor.execute(sql).fetchall()
    return list(map(get_genre_by_row, rows))

  def get_genres_of_book(self, genres):
    cursor = self.connection.session
    sql = "SELECT id, name FROM unnest(:genres) book_genre LEFT JOIN genres g on g.id=book_genre WHERE visible=1"
    rows = cursor.execute(sql, {'genres':genres}).fetchall()
    return list(map(get_genre_by_row, rows))

  def get_genre(self,name):
    cursor = self.connection.session
    sql = "SELECT id, name FROM genres WHERE visible=1 AND name=:name"
    genre = cursor.execute(sql, {'name':name}).fetchone()
    if genre is None:
      return False
    return True
  
  def add_genre(self, genre):
    cursor = self.connection.session
    try:
      sql = "INSERT INTO genres (name, visible) VALUES (:genre, 1)"
      cursor.execute(sql, {"genre":genre})
      cursor.commit()
      return True
    except:
      return False
  
  def hide_genre(self, genre_id):
    cursor = self.connection.session
    try:
      sql = """UPDATE genres SET visible=0 WHERE id=:genre_id"""
      cursor.execute(sql, {"book_id":genre_id})
      cursor.commit()
      return True
    except:
      return False


genre_repository = GenreRepository(database_connection)