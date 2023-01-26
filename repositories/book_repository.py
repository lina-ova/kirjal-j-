from database import database_connection
from entities.book import Book

def get_book_by_row(row):
    return Book(row['id'], row['name'], row["author"], row['description'], \
        row['genres'], row['visible'], row['cover'] ) if row else None

class BookRepository:
  def __init__(self, connection):
    self.connection = connection

  def add_book(self, name, author, description, genres, cover):
    cursor = self.connection.session

    sql = "INSERT INTO books (name, author, description, genres, cover, visible) VALUES (:name, :author, :description, :genres, :cover, 1)"
    cursor.execute(sql, {"name":name, "author":author, "description":description, "genres":genres, "cover":cover})
    cursor.commit()

  def get_books(self):
    """Palauttaa kaikki kirjat listana"""

    cursor = self.connection.session
    sql = """SELECT id, name, author, description, genres, visible, cover FROM books WHERE visible=1 """
    rows = cursor.execute(sql).fetchall()
    return list(map(get_book_by_row, rows))

  def get_searched_books_title(self, query):
    """Palauttaa kirjojen nimeistä haetut tulokset"""

    cursor = self.connection.session
    try:
        sql = """SELECT id, name, author, description, genres, visible, cover FROM books WHERE name LIKE :query AND visible=1 """
        rows = cursor.execute(sql, {"query":"%"+query+"%"}).fetchall()
        return list(map(get_book_by_row, rows))
    except:
        return []
  def get_searched_books_author(self, query):
    """Palauttaa kirjojen nimeistä haetut tulokset"""

    cursor = self.connection.session
    try:
        sql = """SELECT id, name, author, description, genres, visible, cover FROM books WHERE author LIKE :query AND visible=1 """
        rows = cursor.execute(sql, {"query":"%"+query+"%"}).fetchall()
        return list(map(get_book_by_row, rows))
    except:
        return []

  def get_info(self, book_id):
    cursor = self.connection.session
    sql = """SELECT id, name, author, description, genres, visible, cover FROM books WHERE id=:book_id"""
    book = cursor.execute(sql, {"book_id":book_id}).fetchone()

    return Book(book[0],book[1],book[2],book[3],book[4],book[5],book[6])

  def hide_book(self, book_id):
    """Asettaa kirjataulun visible-sarakkeeseen arvon False.
    Metodin avulla voidaan piilottaa haluttu rivi."""

    cursor = self.connection.session
    try:
        sql = """UPDATE books SET visible=0 WHERE id=:book_id"""
        cursor.execute(sql, {"book_id":book_id})
        cursor.commit()
    except:
        return False
    return True
  def get_books_of_genre(self, genre_id):
    """Palauttaa kirjojen nimeistä haetut tulokset"""

    cursor = self.connection.session
    try:
        sql = """SELECT id, name, author, description, genres, visible, cover FROM books WHERE :genre =ANY(genres) AND visible=1 """
        rows = cursor.execute(sql, {'genre':genre_id}).fetchall()
        return list(map(get_book_by_row, rows))
    except:
        return []

  def get_favourites(self, user_id):
    """Palauttaa kirjojen nimeistä haetut tulokset"""
    cursor = self.connection.session
    try:

        sql1 = """SELECT * FROM books WHERE id =ANY((SELECT favourite_books from users WHERE id=:user_id)::int[]) AND visible=1 """
        rows = cursor.execute(sql1, {'user_id':user_id}).fetchall()
        print(rows)
        return list(map(get_book_by_row, rows))
    except:
        return []

book_repository = BookRepository(database_connection)