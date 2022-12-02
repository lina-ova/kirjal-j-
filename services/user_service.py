import secrets
from flask import session
from repositories.user_repository import user_repository as default_user_repository

class UserInputError(Exception):
    pass

class UserService:
    def __init__(self, user_repository = default_user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password, password_confirmation, role):
        self.validate(username, password, password_confirmation)
        if not self._user_repository.get_user(username):
            if self._user_repository.add_user(username, password, role):
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

    def _set_session(self, username):
        role_and_id = self._user_repository.get_info(username)

        session["username"] = username
        session["user_id"] = role_and_id[0]
        session["admin"] = role_and_id[1]
        session["csrf_token"] = secrets.token_hex(16)

    def logout(self):
        del session["username"]
        del session["user_id"]
        del session["admin"] 
        del session["scrf_token"] 

user_service = UserService()