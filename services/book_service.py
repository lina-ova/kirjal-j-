from repositories.book_repository import book_repository as default_book_repository
from flask import session, abort

class UserInputError(Exception):
    pass

class BookService:

  def __init__(self, book_repository=default_book_repository):
    self._book_repository = book_repository

  def add_new_book(self, name, author, description, genres, csrf_token):
    if len(name) < 3 or len(name) > 50:
      raise UserInputError("Anna otsikko 3-50 merkin pituisena")
    if len(author) > 100:
      raise UserInputError("Anna kirjoittajan nimi enintään 100 merkin pituisena")
    if len(description) > 300:
      raise UserInputError("Anna enintään 300 merkin pituinen kuvaus")
    if len(genres) == 0: 
      raise UserInputError("Anna joku genre")
    if session["csrf_token"] != csrf_token:
      abort(403)
    self._book_repository.add_book(name, author, description, genres)
  
  def get_info(self, book_id):
    book = self._book_repository.get_info(book_id)
    if book == None:
        raise UserInputError("Kirjaa ei löytynyt")
    return book

  def get_visible_books(self):
    return self._book_repository.get_books()

  def delete_book(self, book_id, csrf_token):
    if session["csrf_token"] != csrf_token:
      abort(403)
    return self._book_repository.hide_book(book_id)

  def get_searched_books(self, query, option):
    if option==None or query==None:
      return self.get_visible_books()
    print(query, option)
    if option=='name':
      return self._book_repository.get_searched_books_title(query)
    if option=='author':
      return self._book_repository.get_searched_books_author(query)

  def add_stars(self, book_id, stars, csrf_token):
    if book_id==None or stars==None: 
        raise Exception ("jotain meni väärin")
    if session["csrf_token"] != csrf_token:
      abort(403)
    book = self._book_repository.get_info(book_id)
    if book == None:
        raise Exception("Kirjaa ei löytynyt")
    updated = (book.stars + int(stars))/2
    return self._book_repository.add_stars(book_id, updated)

book_service = BookService()