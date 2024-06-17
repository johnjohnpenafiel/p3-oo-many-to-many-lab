class Author:

    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self): 
        """This method should return a list of related contracts."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self): 
        """This method should return a list of related books""" 
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties): 
        """This method should create and return a new Contract object"""
        return Contract(self, book, date, royalties)

    def total_royalties(self): 
        """This method should return the total amount of royalties that 
        the author has earned from all of their contracts."""
        royalty =  [contract.royalties for contract in self.contracts()]
        return sum(royalty)


class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self): 
        """This method should return a list of related contracts."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self): 
        """This method should return a list of related books""" 
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    @classmethod
    def contracts_by_date(cls, date):
        """return all contracts that have the same date as the date passed into the method."""
        return [contract for contract in Contract.all if contract.date == date]
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

    
    