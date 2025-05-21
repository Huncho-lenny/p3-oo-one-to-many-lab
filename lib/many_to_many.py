class Author:

    all = []

    def __init__(self,name: str):
        self.name = name
        Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self] 
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self,book, date, royalties):
        return Contract(self,book,date,royalties)  
    def total_royalties(self):
        total_royalties = [contract.royalties for contract in self.contracts()]
        return sum(total_royalties)
    


class Book:

    all = []

    def __init__(self,title: str):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

   

class Contract:

    all  = []

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author 

    @author.setter
    def author(self,new_author):
        if isinstance(new_author,Author):
            self._author = new_author
        else:
            raise Exception("author must be an instance of Author")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self,new_book):
        if isinstance(new_book,Book):
            self._book = new_book
        else:
            raise Exception("book must be of instance book")

    @property
    def date(self):
        return self._date 
    
    @date.setter
    def date(self,new_date):
        if isinstance(new_date,str):
            self._date = new_date
        else:
            raise Exception("date must be a string")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self,new_royalties):
        if isinstance(new_royalties,(int,float)):
            self._royalties = new_royalties
        else:
            raise Exception("royalties muist be an integer")


    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]

    
   