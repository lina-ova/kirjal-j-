from repositories.review_repository import review_repository as default_review_repository



class ReviewService:
    def __init__(self, review_repository=default_review_repository):
        self._review_repository = review_repository

    def add_review(self, user_id, username, book_id, stars,review):
        if user_id == None or username == None:
            raise Exception ('kirjaudu tai registeröidy ensin')
        if stars == None:
            raise Exception("kerro mielipiteesi kirjasta")
        if book_id == None:
            raise Exception("jotain meni väärin")

        return self._review_repository.add_review(user_id, username, book_id, stars, review)

    def get_visible_reviews(self, book_id):
        reviews = self._review_repository.get_reviews(book_id)
        visible_reviews = [review for review in reviews if review.visible==1]
        return visible_reviews

    def delete_review(self, review_id):
        return self._review_repository.hide_review(review_id)


review_service = ReviewService()