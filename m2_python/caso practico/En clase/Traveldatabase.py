
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
        self.travels.append(travel)
    
    def update(self):
    
    def delete(self):
        
    
    