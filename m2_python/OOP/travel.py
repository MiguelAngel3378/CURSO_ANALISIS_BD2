import datetime

class Travel:
    
    def __init__(self, city_from, city_to, date_from, date_to):
        self.city_from = city_from
        self.city_to = city_to
        self.date_from = date_from
        self.date_to = date_to

date_from = datetime.date.today()
date_to = datetime.date.today()
travel1 = Travel("Madrid", "Praga", date_from, date_to)
print(f'Dia de salida {travel1.date_from} y dia de su llegada {travel1.date_to}')

