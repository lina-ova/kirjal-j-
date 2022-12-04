from database import database_connection
from entities.review import Review

def get_review_by_row(row):
    return Review(row['id'], row['user_id'], row["username"], row["book_id"], row['stars'], \
        row['review'], row['time'], row['visible']) if row else None

class ReviewRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def add_review(self, user_id, username, book_id, stars, review):
        cursor = self.connection.session
        sql = "INSERT INTO reviews (user_id, username, book_id, stars,review, time, visible) VALUES (:user_id, :username, :book_id, :stars, :review, NOW(), 1)"
        try:
            cursor.execute(sql, {"user_id":user_id, "username": username, "book_id":book_id, "stars":stars,"review":review})
            cursor.commit()
        except:
            return False
        return True

    def get_reviews(self, book_id):
        cursor = self.connection.session
        sql = "SELECT id, user_id, username, book_id, stars,review, time, visible FROM reviews WHERE book_id=:book_id AND visible=1"
        rows = cursor.execute(sql, {"book_id":book_id}).fetchall()
        return list(map(get_review_by_row, rows))


    def hide_review(self, review_id):
        """Asettaa kirjataulun visible-sarakkeeseen arvon False.
        Metodin avulla voidaan piilottaa haluttu rivi."""

        cursor = self.connection.session
        try:
            sql = """UPDATE reviews SET visible=0 WHERE id=:review_id"""
            cursor.execute(sql, {"review_id":review_id})
            cursor.commit()
        except:
            return False
        return True
    def hide_reviews(self, book_id):
        """Asettaa kirjataulun visible-sarakkeeseen arvon False.
        Metodin avulla voidaan piilottaa haluttu rivi."""

        cursor = self.connection.session
        try:
            sql = """UPDATE reviews SET visible=0 WHERE book_id=:book_id"""
            cursor.execute(sql, {"book_id":book_id})
            cursor.commit()
        except:
            return False
        return True

    def get_stats(self, book_id):
        cursor = self.connection.session
        try:
          sql = "SELECT COUNT (reviews), sum(stars) FROM reviews WHERE book_id=:book_id AND visible=1"
          reviews = cursor.execute(sql, {"book_id":book_id}).fetchone()
          return reviews
        except:
            return False

review_repository = ReviewRepository(database_connection)