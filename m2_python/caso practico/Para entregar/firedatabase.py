class FireDatabase:
    def __init__(self):
        self.fire = []
        
    def find_all(self): 
        return self.fire.copy()
    
    def find_by_id(self, id):
        for fire in self.fires:
            if fire.id == id:
                return fire        
        return None
