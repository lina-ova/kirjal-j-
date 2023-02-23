from repositories.feedback_repository import feedback_repository as default_feedback_repository
from flask import session, abort

class feedbackService:
  def __init__(self, feedback_repository=default_feedback_repository):
    self._feedback_repository = feedback_repository

  def add_feedback(self, feedback, csrf_token):
    if feedback == None: 
      raise Exception ('Jokin meni vikaan')
    if session['username']== None:
      raise Exception ('kirjaudu tai registeröidy ensin')
    if len(feedback)<3 or len(feedback)>5000:
      raise Exception ('anna kunnon palautteen')
    if session["csrf_token"] != csrf_token:
      abort(403)
    username = session['username']
    return self._feedback_repository.add_feedback(username,feedback)
  def get_visible_feedback(self):
    return self._feedback_repository.get_feedback()

  def delete_feedback(self, feedback_id, csrf_token):
    if session["csrf_token"] != csrf_token or session['admin']!=1:
      abort(403)
    return self._feedback_repository.hide_feedback(feedback_id)


feedback_service = feedbackService()