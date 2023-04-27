
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
        travel.id = 
        
        # asignarle el travel encontrado los valores del travel parametro
    
    def delete(self):
        
    
    