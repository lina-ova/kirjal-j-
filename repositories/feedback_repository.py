from database import database_connection

class FeedbackRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_feedback(self, user_id, feedback):
        cursor = self.connection.session
        sql = "INSERT INTO feedback (user_id, feedback, visible) VALUES (:user_id, :feedback, 1);"
        cursor.execute(sql, {'user_id':user_id, 'feedback':feedback})
        cursor.commit()
        return True


feedback_repository = FeedbackRepository(database_connection)