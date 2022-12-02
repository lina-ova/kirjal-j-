from flask import abort, session
from repositories.review_repository import review_repository as default_review_repository

class ReviewService:
  def __init__(self, review_repository=default_review_repository):
    self._review_repository = review_repository

  def add_review(self, book_id, stars,review, scrf_token):
    if stars == None:
        raise Exception("kerro mielipiteesi kirjasta")
    if book_id == None:
        raise Exception("jotain meni väärin")
    if session["csrf_token"] != scrf_token:
      abort(403)
    if session['user_id']== None or session['username'] == None:
      raise Exception("Kirjaudu tai registeröidy ensin")
    user_id=session['user_id']
    username=session['username']

    return self._review_repository.add_review(user_id, username, book_id, stars, review)

  def get_visible_reviews(self, book_id):
    return self._review_repository.get_reviews(book_id)

  def delete_review(self, review_id, csrf_token):
    if session["csrf_token"] != csrf_token:
      abort(403)
    return self._review_repository.hide_review(review_id)

  def delete_reviews_of_book(self, book_id, csrf_token):
    if session["csrf_token"] != csrf_token:
      abort(403)
    return self._review_repository.hide_reviews(book_id)

review_service = ReviewService()