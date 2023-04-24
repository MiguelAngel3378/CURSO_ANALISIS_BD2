
class Ordenador:
    
    def __init__(self, fabricante, modelo, anio, precio, estado):
        self.fabricante = fabricante
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.estado = estado
        
    def encender (self):
        self.estado = True
        
    def aplicar_descuento(self, descuento):
        if (descuento > 0 and descuento < 0.9):
        self.precio = self.precio - self.precio * descuento
    

ordenador1 = Ordenador("Asus", "ASSA",2000, 495 )
ordenador1.precio = 0.9

ordenador2 = Ordenador("MSI", "HP", 2021, 955)
ordenador2.estado = True 

ordenador2.encender= ()
ordenador2.aplicar_descuento(0.10)
ordenador2.aplicar_descuento(-0.4)    
        