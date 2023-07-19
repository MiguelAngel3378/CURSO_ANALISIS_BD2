
from FireDatabase import FireDatabase

def main():
    db = FireDatabase()
    while True:
        print("Menú de opciones:")
        print("1. Mostrar todos los incendios")
        print("2. Buscar incendio por id")
        print("3. Buscar incendios por nivel")
        print("4. Buscar incendios por atributo")
        print("5. Guardar nuevo incendio")
        print("6. Actualizar incendio")
        print("7. Borrar incendio por id")
        print("8. Salir")
        option = int(input("Introduce una opción: "))
        if option == 1:
            fires = db.find_all()
            for fire in fires:
                print(fire.__dict__)
        elif option == 2:
            id = int(input("Introduce el id del incendio: "))
            fire = db.find_by_id(id)
            if fire is not None:
                print(fire.__dict__)
            else:
                print("No se encontró el incendio con el id especificado")
        elif option == 3:
            level = input("Introduce el nivel del incendio: ")
            fires = db.find_by_level(level)
            for fire in fires:
                print(fire.__dict__)
        elif option == 4:
            attribute = input("Introduce el atributo del incendio: ")
            fires = db.find_by_attribute(attribute)
            for fire in fires:
                print(fire.__dict__)
        elif option == 5:
            level = input("Introduce el nivel del incendio: ")
            attribute = input("Introduce el atributo del incendio: ")
            new_fire = db.save(level, attribute)
            print(f"Se guardó el nuevo incendio con id {new_fire.id}")
        elif option == 6:
            id = int(input("Introduce el id del incendio a actualizar: "))
            level = input("Introduce el nuevo nivel del incendio (deja en blanco para no actualizar): ")
            attribute = input("Introduce el nuevo atributo del incendio (deja en blanco para no actualizar): ")
            updated = db.update(id, level or None, attribute or None)
            if updated:
                print(f"Se actualizó el incendio con id {id}")
            else:
                print(f"No se encontró el incendio con el id especificado")
        elif option == 7:
            id = int(input("Introduce el id del incendio a borrar: "))
            deleted = db.delete_by_id(id)
            if deleted:
                print(f"Se borró el incendio con id {id}")
            else:
                print(f"No se encontró el incendio con el id especificado")
        elif option == 8:
            break

if __name__ == "__main__":
    main()