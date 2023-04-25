import datetime

class User:
    
    def __init__(self, id, nif, birthday, email, phone, password="admin"):
        self.id = id
        self.nif = nif
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.password = password
        
        
user1 = User(1,'6534387Y', datetime.date,{1995, 1, 23}, 'user1@gmail.com', '680924086')
user2 = User(2,'6534387Z', datetime.date.fromisoformat,{"1995-02-23"}, 'user2@gmail.com', '6809240867')      
        
print(user1.birthday)
print(user2.birthday)
