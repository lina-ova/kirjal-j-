class Book:
    def __init__(self, id, name, author, description, genres, visible, cover=None):
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.genres = genres
        self.visible = visible
        self.cover = cover
