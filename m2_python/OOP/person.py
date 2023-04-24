

class Person:
    
    def _init_(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        

person1 = Person(1,'person1', 'apellido1')

print(f'Persona tiene atribusto: {person1.id}, {person1.first_name}, {person1.last_name}')

person2 = Person(2, 'person2', 'apellido2')
