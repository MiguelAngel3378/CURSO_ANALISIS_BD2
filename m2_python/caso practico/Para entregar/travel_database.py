class TravelDatabase:
    def __init__(self):
        self.travels = []
    
        def find_all(self): 
         return self.travels.copy()
        
            
    def find_by_id(self, id):
        # iterar sobre los viajes
        for travel in self.travels:
            if travel.id == id:
                return travel
            
        return None
    
    
    
    def find_all_by_city(self, city_from, city_to):
        filtered_travels = [] 
        
        for travel in self.travels:
            if travel.city_from == city_from and travel.city_to == city_to:
                filtered_travels.append(travel)
                
        return filtered_travels
    
    
    
    def save(self, travel):
        
        id_maximo = 0
        for current_travel in self.travels:
            if current_travel.id > id_maximo:
                id_maximo = current_travel.id
        
        
        travel.id = id_maximo + 1
        
        
        self.travels.append(travel)
            
    def update(self, travel):
        
        for current_travel in self.travels:
            if current_travel.id == travel.id:
                current_travel.city_from = travel.city_from
                current_travel.city_to = travel.city_to
                current_travel.passengers = travel.passengers
                current_travel.price = travel.price
                return True

        return False
    
    
    def delete_by_id(self, id):
        for travel in self.travels:
            if travel.id == id:
                self.travels.remove(travel)
                break
                
    def delete_all(self): 
        self.travels = []
        