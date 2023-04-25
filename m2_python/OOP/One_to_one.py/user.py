import datetime

class User:

    def __init__(self, id, nif, birthday, email, phone, adress, password="admin"):
        self.id = id
        self.nif = nif
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.adress = adress    
        self.password = password


user1 = User(1, '6534387Y', datetime.date(1995, 1, 23), 'user1@gmail.com', '680924086')
user2 = User(2, '6534387Z', datetime.date.fromisoformat("1995-02-23"), 'user2@gmail.com', '6809240867')


print(user1.id, user1.nif, user1.email)
print(user2.id, user2.nif, user2.email)

class Adress:
    
    def __init__(self, id, street, postal_code, city, country):
        self.id = id
        self.street = street
        self.city = city
        self.country = country
        if (len(postal_code) ==5):
            self.postal_code = postal_code
        else:
            self.postal_code = "28002"

adress1 = Adress(1, "Calle falsa 123", "33021", "Leon", "Spain")
adress2 = Adress(2, "Calle falda 321", "66666666", "Madrid", "Spain")

print(adress1.id, adress1.street, adress1.country)
print(adress2.city, adress2.street)

