from repositories.feedback_repository import feedback_repository as default_feedback_repository
from flask import session, abort

class feedbackService:
  def __init__(self, feedback_repository=default_feedback_repository):
    self._feedback_repository = feedback_repository

  def add_feedback(self, feedback, csrf_token):
    if feedback == None: 
      raise Exception ('Jokin meni vikaan')
    if session['user_id']== None:
      raise Exception ('kirjaudu tai registeröidy ensin')
    if len(feedback)<3 or len(feedback)>5000:
      raise Exception ('anna kunnon palautteen')
    if session["csrf_token"] != csrf_token:
      abort(403)
    user_id = session['user_id']
    return self._feedback_repository.add_feedback(user_id,feedback)


feedback_service = feedbackService()