class Book():

    # class attribute
    all = []

    # constructor
    def __init__(self, isbn, title, author, page_count):
        self._isbn = isbn

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
        
        Book.all.append(self) # appends instance to class attribute upon creation

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

# book1 = Book(1234, "where the red fern grows", "jane smith", 123)

# book2 = Book(5678, "twilight", "stephanie meyer", 350)

book3 = Book(9090, "lord of the rings", "j r r tolkein", 1100)

# for book in Book.all:
#     book.check_out()