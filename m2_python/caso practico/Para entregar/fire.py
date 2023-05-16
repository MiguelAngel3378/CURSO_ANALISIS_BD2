

class Fire:
    def __init__(sel, id, street, city, province,  level, date_from, date_to, active, cause);
        self.id = id
        self.street = street
        self.city = city
        self.province = province
        self.level = level
        self.date_from = date_from
        self.dato_to = date_to
        self.active = active
        self.cause = cause
        
     def __str__(self):
     return f"{self.id} {self.province} {self.street} {self.fire_level}{self.date_from} {self.date_to} {self.active} {self.cause}"
        
primer_incendio = Fire("uno", "Madrid", "Calle Camino de Santiago 15", "low", "02/10/2010", "02/20/2010", "no", "cigarrette")
print(type(primer_incendio))

print(primer_incendio.cause)
print(primer_incendio.fire_level)  
print(primer_incendio.street)  
print(primer_incendio.id)  
