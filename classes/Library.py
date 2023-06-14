class Library():

    def __init__(self, branch_name, county, number_of_staff):
        
        # will work, however not in-depth data check
        '''
        self.branch_name = branch_name
        self.county = county
        self.number_of_staff = number_of_staff
        '''

        self.list_of_books = []

        # in-depth data check
        if isinstance(branch_name, str) and len(branch_name) >= 5:
            self._branch_name = branch_name
        else:
            raise Exception
        
        if isinstance(county, str) and len(county) >= 1 and len(county) <= 20:
            self._county = county
        else:
            raise Exception
        
        if isinstance(number_of_staff, int) and number_of_staff >= 1:
            self._number_of_staff = number_of_staff
        else:
            raise Exception

    @property
    def branch_name(self):
        return self._branch_name
    
    @branch_name.setter
    def branch_name(self, branch_name):
        if isinstance(branch_name, str) and len(branch_name) >= 5:
            self._branch_name = branch_name
        else:
            raise Exception
        
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, county):
        if isinstance(county, str) and len(county) >= 1 and len(county) <= 20:
            self._county = county
        else:
            raise Exception
        
    def get_number_of_staff(self):
        return self._number_of_staff
    
    def set_number_of_staff(self, number_of_staff):
        if isinstance(number_of_staff, int) and number_of_staff >= 1:
            self._number_of_staff = number_of_staff
        else:
            raise Exception
        
    number_of_staff = property(get_number_of_staff, set_number_of_staff)

    def add_a_book(self, book):
        from Book import Book

        if book and isinstance(book, Book): # checks if inputted book is instance of Book class
            self.list_of_books.append(book)
        else:
            raise Exception

bpl = Library("Boston Public Library", "Boston", 100)

from Book import Book

from Book import book3 

fern = Book(1234, "where the red fern grows", "john smith", 150)
twi = Book(5678, "twilight", "stephanie meyer", 350)

bpl.add_a_book(fern)
bpl.add_a_book(twi)
bpl.add_a_book(book3)

for book_in_lib in bpl.list_of_books:
    print(book_in_lib)