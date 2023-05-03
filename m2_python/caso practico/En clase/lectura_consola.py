
while True:

    print(""" App de viajes
          1 - Consultar viajes
          2 - Consultar un viaje por id
          3 - Consultar un viaje por ciudad
          4 - Crear un nuevo viaje
          5 - Actualizar un viaje existente 
          6 - Borrar un viaje por id
          7 - Borrar todos los viajes
          8 - Salir de la aplicación \n
          """)
    option = int(input("Introduce una opción\n"))
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4: # crear un nuevo Travel
        
        city_from = input("Introduce la ciudad origen")
        city_to = input("Introduce la ciudad origen")
        
        # Leer passengers
        leido = False
        while not leido:
            try:
                passengers = int(input("Introduce passengers"))
                leido = True
            except ValueError:
                print("Número de pasajeros erróneo")
            
        # Leer precio
        leido = False
        while not leido:
            try:
                price = float(input("Introduce precio"))
                leido = True
            except ValueError:
                print("Precio erróneo")
        
        
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:   
        pass
    else:
        print('Hasta la proxima')
        break