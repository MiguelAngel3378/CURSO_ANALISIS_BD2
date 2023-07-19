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

    def find_by_level(self, level):
        return [fire for fire in self.fires if fire.level == level]
    
    def find_by_attribute(self, attribute):
        return [fire for fire in self.fires if fire.attribute == attribute]
    
    def save(self, level, attribute):
        id = max([fire.id for fire in self.fires], default=0) + 1
        new_fire = Fire(id, level, attribute)
        self.fires.append(new_fire)
        return new_fire
    
    def update(self, id, level=None, attribute=None):
        fire = self.find_by_id(id)
        if fire is not None:
            if level is not None:
                fire.level = level
            if attribute is not None:
                fire.attribute = attribute
            return True
        return False