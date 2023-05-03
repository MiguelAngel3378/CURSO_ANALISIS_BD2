
class Traveldatabase:
    def __int__(self):
        self.travels = []
    
    # SELECT * FROM travels
    def find_all(self): 
        return self.travels.copy()
    
    # SELECT * FROM travels WHERE id = x
        # iterar sobre los viajes
        # el contral el viaje por id
        # devolver el viaje encontrado
        
    def find_by_id(self): 
        for travel in self.travels:
            if travel.id == id:
                return travel
        return None
    
    # SELECT * FROM travels
    # WHERE city_from = "" AND city_to = ""
    
    def find_all_by_city(self, city_from, city_to):
        filtered_travels = []
        for travel in self.travels:
            if travel.city_from == city_from and travel.city_to == city_to:
                filtered_travels.append(travel)
                
        return filtered_travels
        
    def save(self, travel):
        # buscar en travels cual es el id mas alto
        id_maximo = 0
        for current_travel in self.travels:
            if current_travel.id > id_maximo:
                id_maximo = current_travel.id
        
        # generar el nuevo id sumando 1 al id mas alto  
    
        travel.id = id_maximo + 1
        
        # gusrdar en la lista
        self.travels.append(travel)
    
    def update(self, travel):
        # encontrar el travel a actualizar
        for current_travel in self.travels:
            if current_travel.id == travel.id:
                current_travel.city_from = travel.city_from
                current_travel.city_to = travel.city.to
                current_travel.passengers = travel.passengers
                current_travel.price = travel.price
                return True
            
        return False
        
        # asignarle el travel encontrado los valores del travel parametro
    
    def delete_by_id(self, id):
        for travel in self.travels:
            if travel.id == id:
                self.travels.remove
                
        # DELETE FROM travels WHERE id = 1
    def delete_by_id(self, id):
        for travel in self.travels:
            if travel.id == id:
                self.travels.remove(travel)
                break
                
    def delete_all(self): 
        self.travels = []
                
        # Crear 1 objeto TravelDatabase
    from travel_database import Traveldatabase
    travel_database = Traveldatabase()
    
        # Crear 5 objetos Travel utilizando el constructor
    from Travel import Travel 
    travel1 = Travel(city_from=  'Madrid', city_to='Barcelona', price=123.11, passengers=2)
    travel2 = Travel(city_from=  'Asturias', city_to='Malaga', price=223.11, passengers=3)  
        
        # Insertar los objetos Travel en TravelDatabase utilizando base()
    travel_database.save(travel1)
    
        # Ejempko de como capturar un error
    travels = travel_database.find_all_by_city
        
        # Probar metodos find
        
    travels = travel_database.find_all()
    print(f"Longitud {len(travels)}")
    print(f"Viaje 1 {travels[0]}")
    print(f"Viaje 2 {travels[1]}")
    
    travel2 = travel_database.find_by_id(2)
    print(f"Viaje 2: {travel2}")
    
    travel9 = travel_database.find_by_id(9)
    print(f"Viaje 9: {travel9}")
        # Probar metodo update
        
        
        # Probar delete & deleteall
        
        
    
    