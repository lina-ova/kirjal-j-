from database import database_connection
from entities.feedback import Feedback


def get_feedback_by_row(row):
    return Feedback(row['id'],row['username'], row['feedback'], row['time']) if row else None
class FeedbackRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_feedback(self, username, feedback):
        cursor = self.connection.session
        sql = "INSERT INTO feedback (username, feedback, time, visible) VALUES (:username, :feedback, NOW(), 1);"
        try:
            cursor.execute(sql, {'username':username, 'feedback':feedback})
            cursor.commit()
            return True
        except:
            return False
    def get_feedback(self):
        """Palauttaa palautteet listana"""

        cursor = self.connection.session
        sql = """SELECT id, username, feedback, time FROM feedback WHERE visible=1 """
        rows = cursor.execute(sql).fetchall()
        return list(map(get_feedback_by_row, rows))
    def hide_feedback(self, feedback_id):
        print(feedback_id)
        """Asettaa feedbacktaulun visible-sarakkeeseen arvon False.
        Metodin avulla voidaan piilottaa haluttu rivi."""

        cursor = self.connection.session
        try:
            sql = """UPDATE feedback SET visible=0 WHERE id=:_id"""
            cursor.execute(sql, {"_id":feedback_id})
            cursor.commit()
        except:
            return False
        return True


feedback_repository = FeedbackRepository(database_connection)