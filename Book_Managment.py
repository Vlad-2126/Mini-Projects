class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "ready"
    
    def __str__(self):
        return f"The book is called'{self.title}', was writn by {self.author} in {self.year}"
    
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