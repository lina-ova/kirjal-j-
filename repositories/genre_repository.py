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
        sql = "SELECT id, name FROM unnest(:genres) book_genre LEFT JOIN genres g on g.id=book_genre"
        rows = cursor.execute(sql, {'genres':genres}).fetchall()
        return list(map(get_genre_by_row, rows))


genre_repository = GenreRepository(database_connection)