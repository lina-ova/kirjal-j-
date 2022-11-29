class Review:
    def __init__(self, id, user_id, username, book_id, stars, review, time, visible):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.book_id = book_id
        self.review = review
        self.stars = stars
        self.time = time
        self.visible = visible