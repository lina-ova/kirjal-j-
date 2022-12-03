import secrets
from flask import session, abort
from repositories.user_repository import user_repository as default_user_repository

class UserInputError(Exception):
    pass

class UserService:
  def __init__(self, user_repository = default_user_repository):
    self._user_repository = user_repository

  def create_user(self, username, password, password_confirmation):
    self.validate(username, password, password_confirmation)
    if not self._user_repository.get_user(username):
        if self._user_repository.add_user(username, password):
            return True
    else:
        raise UserInputError("Käyttäjätunnus on jo olemassa.")

  def validate(self, username, password, password_confirmation):
    if not username or not password or not password_confirmation:
        raise UserInputError("Kaikkia kenttiä ei ole täytetty.")
    if password != password_confirmation:
        raise UserInputError("Salasana ja salasanan vahvistus eivät täsmää.")

  def login(self, username, password):
    if not self._user_repository.check_password(username, password):
        raise UserInputError('Käyttäjätunnus tai salasana eivät täsmää')
    self._set_session(username)

  def fav_book(self,id_fav, id_unfav, csrf_token):
    if id_fav==None and id_unfav==None:
      raise Exception('Jotain meni vikaan')
    if session['user_id'] == None:
      raise Exception('Kirjaudu tai registeröidy ensin')
    if session["csrf_token"] != csrf_token:
      abort(403)
    if id_fav !=None:
      success = self._user_repository.book_favourite(user_id = session['user_id'], book_id=id_fav)
    if id_unfav !=None:
      success = self._user_repository.book_unfavourite(user_id = session['user_id'], book_id=id_unfav)
    
    if success:
      self._set_session(session['username'])
      return True
    return False


  def _set_session(self, username):
    info = self._user_repository.get_info(username)

    session["username"] = username
    session["user_id"] = info[0]
    session["admin"] = info[1]
    session["favourites"] = info[2] or []
    session["csrf_token"] = secrets.token_hex(16)

  def logout(self):
    del session["username"]
    del session["user_id"]
    del session["admin"] 
    del session["csrf_token"] 

user_service = UserService()