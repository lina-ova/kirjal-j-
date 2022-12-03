from database import database_connection

class UserRepository:
  def __init__(self, connection):
    self.connection = connection

  def add_user(self, username, password):
    cursor = self.connection.session
    sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, 0)"
    try:
        cursor.execute(sql, {"username": username, "password": password})
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
    sql = "SELECT id, admin, favourites FROM users WHERE username=:username"
    result = cursor.execute(sql, {"username":username}).fetchone()
    user_id = result[0]
    admin = result[1]
    favourites=result[2] 
    return user_id, admin, favourites
  
  def book_favourite(self, user_id, book_id):
    cursor = self.connection.session
    sql = """UPDATE users SET favourites = array_append(favourites, :book_id) WHERE id=:user_id """
    try:
      cursor.execute(sql, {"book_id":book_id, "user_id":user_id})
      cursor.commit()
    except:
      return False
    return True
  
  def book_unfavourite(self, user_id, book_id):
    cursor = self.connection.session
    sql = """UPDATE users SET favourites = array_remove(favourites, :book_id) WHERE id=:user_id """
    try:
      cursor.execute(sql, {"book_id":book_id, "user_id":user_id})
      cursor.commit()
    except:
      return False
    return True


user_repository = UserRepository(database_connection)