
class Book:
    def __init__(self, title, num_page):
        self.title = title
        self.num_page = num_page
        
    def __str__(self):
        return f'title={self.title}, num_pages={self.num_pages}'
    
book1 = Book('book1, 340')
print(book1)
