# class CapitalName:
#     def __set_name__(self,owner,name):
#         self.name = "_" + name
        
#     def __get__(self,instance,owner):
#         return instance.__dict__[self.name].capitalize()
    
#     def __set__(self,instance,value):
#         raise TypeError(f"{self.name} can not be changed")
    
class Book: # A simple class to represent a book in the library
    book_dict = {} # Placeholder for storing books (will be used later)
    
    # title = CapitalName()
    # author = CapitalName()
    
    def __init__(self,title,author,year):
        self._title = title
        self._author = author
        self.year = year
        self._status = None
    
    def __str__(self):
        return f"The book is called '{self._title}', was writn by {self._author} in {self.year}"
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value.lower() not in ["available","borrowed"]:
            raise ValueError("Invalide status name")
        self._status = value.lover()
    
    # @staticmethod
    # def add_book(title,author,year):
    #     Book.book_dict[title] = Book(title,author,year)
    
class User: # A simple class to represent a library user
    user_dict = {} # Placeholder for storing users (will be used later)
    
    def __init__(self,name,user_id):
        self.name = name
        self._user_id = user_id
        
    
    def __str__(self):
        return f"User name: {self.name}, user id: {self._user_id}"
    
    # @property
    # def user_id(self):
    #     if self._user_id in User.user_dict.keys():
    #         raise ValueError("ID must be unique")
    #     return self._user_id
    
    # @staticmethod
    # def add_user(name,user_id):
    #     User.user_dict[user_id] = User(name,user_id)

