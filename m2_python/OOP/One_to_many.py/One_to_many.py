
class Book:
    def __init__(self, title, num_page):
        self.title = title
        self.num_page = num_page
        
        
class Autor:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.books = []
        
book1 = Book('book100', 350)
book2 = Book('book200', 450)

author1 = Autor('author1', 2005)

books = []

print('fin')
