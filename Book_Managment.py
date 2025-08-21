class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "ready"
    
    def __str__(self):
        return f"The book is called'{self.title}', was writn by {self.author} in {self.year}"
    
