
# nombre = input("Introdusca su nombre\n")

# edad = int(input("Introduce edad\n"))

# salary = float(input("Introduce salario\n"))

# apto = bool(int(input("0 Es no apto y 1 es apto\n")))

# fecha_nacimiento = input("Introduce fecha de nacimiento (YYYY-MM-dd) (1990-07-20) \n")
import datetime

fecha_nacimiento_str = input("Introduce fecha nacimiento (dd/MM/YYYY) (03/11/1991) \n")
fecha_array = fecha_nacimiento_str.split("/")
year = int(fecha_array[2])
month = int(fecha_array[1])
day = int(fecha_array[0])
fecha_final = datetime.date(year, month, day)

print("fin")



