from database import database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_user(self, username, password, role):
        cursor = self.connection.session
        sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
        try:
            cursor.execute(sql, {"username": username, "password": password, "admin":role})
            cursor.commit()
        except:
            return False
        return True

    def get_user(self, username):
        cursor = self.connection.session
        sql = "SELECT username FROM users WHERE username=:username"
        result = cursor.execute(sql, {"username":username})
        user = result.fetchone()
        if user is None:
            return False
        return True

    def check_password(self, username, password):
        cursor=self.connection.session
        sql = "SELECT password FROM users WHERE username=:username and password=:password"
        result = cursor.execute(sql, {"username":username, "password":password})
        password = result.fetchone()
        if password is None:
            return False
        return True

    def get_info(self, username):
        cursor=self.connection.session
        sql = "SELECT id, admin FROM users WHERE username=:username"
        result = cursor.execute(sql, {"username":username}).fetchone()
        user_id = result[0]
        admin = result[1]
        return user_id,admin

user_repository = UserRepository(database_connection)