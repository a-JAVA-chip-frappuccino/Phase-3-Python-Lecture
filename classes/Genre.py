class Genre():

    def __init__(self, id, genre):
        self.id = id
        self.genre = genre

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            raise Exception
        
    def __str__(self):
        return f"Genre: {self._genre}"
        
scifi = Genre(1, "science fiction")
romance = Genre(2, "romance")
horror = Genre(3, "horror")
nonfic = Genre(4, "nonfiction")