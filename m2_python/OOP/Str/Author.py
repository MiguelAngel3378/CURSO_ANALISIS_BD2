
class Author:
    def __init__(self, id, nif, email, year, city, num_books):
        self.id = id
        self.nif = nif
        self.email = email
        self.year = year
        self.city = city
        self.num_books = num_books

    def __str__(self):
        
        # OPCION 1:
        # return f"Author con id = {self.id} " \
        # f"nif = {self.nif} " \
        # f"email = {self.email} " \
        # f"year = {self.year} " \
        # f"city = {self.city} " \
        # f"num_books = {self.num_books}"

        # OPCION 2:
        return 'Autor %s %s %s %s' % (self.nif, self.email, self.email, self.year)

author1 = Author(1, '2322323R', 'author1@email.com', 2000, 'Madrid', 20)
print(author1)
