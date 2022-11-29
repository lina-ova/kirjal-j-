from database import database_connection
from entities.book import Book

def get_book_by_row(row):
    return Book(row['id'], row['name'], row["author"], row['description'], \
        row['genre'], row['stars'], row['visible']) if row else None

class BookRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_book(self, name, author, description, genre, stars=0, visible=1):
        cursor = self.connection.session
        sql = "INSERT INTO books (name, author, description, genre, stars, visible) VALUES (:name, :author, :description, :genre, :stars, :visible)"
        cursor.execute(sql, {"name":name, "author":author, "description":description, "genre":genre, "stars":stars, "visible":visible})
        cursor.commit()

    def get_books(self):
        """Palauttaa kaikki kirjat listana"""

        cursor = self.connection.session
        sql = """SELECT id, name, author, description, genre, stars, visible FROM books"""
        cursor.execute(sql)
        rows = cursor.execute(sql).fetchall()
        return list(map(get_book_by_row, rows))

    def get_searched_books(self, query):
        """Palauttaa kirjojen nimeistä haetut tulokset"""

        cursor = self.connection.session

        try:
            sql = """SELECT id, name, author, description, genre, stars, visible FROM books WHERE name LIKE :query AND visible=1"""
            rows = cursor.execute(sql, {"query":"%"+query+"%"}).fetchall()
            return list(map(get_book_by_row, rows))
        except:
            return []
        return rows

    def get_info(self, book_id):
        cursor = self.connection.session


        sql = """SELECT id, name, author, description, genre, stars, visible FROM books WHERE id=:book_id"""
        book = cursor.execute(sql, {"book_id":book_id}).fetchone()

        return Book(book[0],book[1],book[2],book[3],book[4],book[5],book[6])

    def hide_book(self, book_id):
        """Asettaa kirjataulun visible-sarakkeeseen arvon False.
        Metodin avulla voidaan piilottaa haluttu rivi."""

        cursor = self.connection.session
        try:
            sql = """UPDATE books SET visible=:visible WHERE id=:book_id"""
            cursor.execute(sql, {"visible":0, "book_id":book_id})
            cursor.commit()
        except:
            return False
        return True

    def add_stars(self, book_id, stars):
        """lisää kirjalle updated arvo tehtejä review:sta"""

        cursor = self.connection.session
        try:
            sql = """UPDATE books SET stars=:stars WHERE id=:book_id"""
            cursor.execute(sql, {"stars": stars, "book_id":book_id})
            cursor.commit()
        except:
            return False
        return True

book_repository = BookRepository(database_connection)