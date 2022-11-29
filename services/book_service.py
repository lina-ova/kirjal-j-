from repositories.book_repository import book_repository as default_book_repository



class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository

    def add_new_book(self, admin, name, author, description, genre):
        if admin != 1:
            raise Exception ('sinulla ei ole oikeuksia tähän toimintoon')
        if len(name) < 3 or len(name) > 50:
            raise Exception("Anna otsikko 3-50 merkin pituisena")
        if len(author) > 100:
            raise Exception("Anna kirjoittajan nimi enintään 100 merkin pituisena")
        if len(description) > 300:
            raise Exception("Anna enintään 300 merkin pituinen kuvaus")
        if len(genre) < 3 or len(genre) > 50: 
            raise Exception("Anna genre 3-50 merkin pituisena")
        self._book_repository.add_book(name, author, description, genre)
    
    def get_info(self, book_id):
        book = self._book_repository.get_info(book_id)
        if book == None:
            raise Exception("Kirjaa ei löytynyt")
        return book

    def get_visible_books(self):
        books = self._book_repository.get_books()
        visible_books = [book for book in books if book.visible==1]
        return visible_books

    def delete_book(self, book_id):
        return self._book_repository.hide_book(book_id)

    def get_searched_books(self, query):

        return self._book_repository.get_searched_books(query)

    def add_stars(self, book_id, stars):
        if book_id==None or stars==None: 
            raise Exception ("jotain meni väärin")
        book = self._book_repository.get_info(book_id)
        if book == None:
            raise Exception("Kirjaa ei löytynyt")
        updated = (book.stars + int(stars))/2
        return self._book_repository.add_stars(book_id, updated)

book_service = BookService()