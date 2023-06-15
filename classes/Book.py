class Book():

    # class attribute
    all_books = []

    # constructor
    def __init__(self, isbn, title, author, page_count):
        self._isbn = isbn
        self.genre = ""

        if type(title) == str and len(title) > 1:
            self._title = title
        else:
            raise Exception
        
        if isinstance(author, str) and len(author) > 3:
            self._author = author
        else:
            raise Exception
        
        if type(page_count) == int and page_count >= 1:
            self._page_count = page_count
        else:
            raise Exception
        
        Book.all_books.append(self) # appends instance to class attribute upon creation

    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, isbn):
        self._isbn = isbn

    isbn = property(get_isbn, set_isbn)

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if type(title) == str and len(title) > 1:
            self._title = title
        else:
            raise Exception
        
    title = property(get_title, set_title)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author) > 3:
            self._author = author
        else:
            raise Exception
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int and page_count >= 1:
            self._page_count = page_count
        else:
            raise Exception
        
    # instance method
    def check_out(self):
        print("You've checked out " + self._title + "!")
        return self
    
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}"
    
    def give_a_genre(self, inputted_genre):
        from Genre import Genre

        if inputted_genre and isinstance(inputted_genre, Genre):
            self.genre = inputted_genre
        else:
            raise Exception

hitchhiker = Book(1234, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 320)
leibowitz = Book(2345, "A Canticle for Leibowitz", "P. Sherman", 300)
bridgerton = Book(3456, "Bridgerton", "W WW", 200)
wib = Book(4567, "The Woman in Black", "fjjif we", 100)
jdc = Book(5678, "Jews Don't Count", "David Baddiel", 120)

from Genre import scifi
from Genre import romance
from Genre import horror
from Genre import nonfic

hitchhiker.give_a_genre(scifi)
leibowitz.give_a_genre(scifi)
bridgerton.give_a_genre(romance)
wib.give_a_genre(horror)
jdc.give_a_genre(nonfic)