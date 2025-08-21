class CapitalName:
    def __set_name__(self,owner,name):
        self.name = "_" + name.capitalize()
        
    def __get__(self,instance,owner):
        return instance.__dict__[self.name]
    
    def __set__(self,instance,value):
        raise TypeError(f"{self.name} can not be changed")
    

class Book:
    book_dict = {}
    
    title = CapitalName()
    author = CapitalName()
    
    def __init__(self,title,author,year):
        self._title = title
        self._author = author
        self.year = year
        self.status = "ready"
    
    def __str__(self):
        return f"The book is called'{self.title}', was writn by {self.author} in {self.year}"
    
    @staticmethod
    def add_book(title,author,year):
        Book.book_dict[title] = Book(title,author,year)
    
class User:
    user_dict = {}
    
    def __init__(self,name,user_id):
        self.name = name
        self._user_id = user_id
        
    
    def __str__(self):
        return f"User name: {self.name}, user id: {self.user_id}"
    
    @property
    def user_id(self):
        if self._user_id in User.user_dict.keys():
            raise ValueError("ID must be unique")
        return self._user_id
    
    @staticmethod
    def add_user(name,user_id):
        User.user_dict[user_id] = User(name,user_id)

Book.add_book("war and peac","tolstoi",1800)
print(Book.book_dict)
User.add_user("Oleg",111)
print(User.user_dict)
# print(Book.book_dict["war and peac"])
# print(User.user_dict[111])