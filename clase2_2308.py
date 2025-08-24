## Variables
# Operador de asignacion =
nombre = "Jesus"
edad = 28

# print(nombre)
# print(edad)

### Tipos de datos fundamentales de datos

#Números -> int - float 
num1 = 25 # int
num2 = 5.5 # float
# print(f"Value: {num1}, Type: {type(num1)}")
# print(f"Value: {num2}, Type: {type(num2)}")

# String -> str -> texto '', ""

ciudad = "Caracas"
nacionalidad = 'Venezolano'
cedula = '26787140'

# print(f"'ciudad' Value: {ciudad}, Type: {type(ciudad)}")
# print(f"Value: {nacionalidad}, Type: {type(nacionalidad)}")
# print(f'"cedula" Value: {cedula}, Type: {type(cedula)}')

paragraph = """
    Hola a
    Todos
    sigo por 
    acá
"""

# print(f"Párrafo: {paragraph}, Type: {type(paragraph)}") 

# Boolean -> bool -> True, False
es_estudiante = False
no_estudiante = True

# print(f"Value: {es_estudiante}, Type: {type(es_estudiante)}")
# print(f"Value: {no_estudiante}, Type: {type(no_estudiante)}")


### Estructuras de datos -> Listas, Tuplas, Diccionarios, Sets

# Listas -> list -> Colecciones de datos -> []
# Las listas (list) -> son mutables

alumnos = ["Carlos", "Jose", "Hendrik"]

# print(alumnos)
# print(alumnos[2])

numeros = [1, 2, 300, 454, 5, 6, 7, 8, 9, 10]
# print(numeros)
# print(numeros[3])

a = "Anzoategui"
b = "Barquisimeto"
c = "Caracas"

# datos = [1, "Hola", 3.5, True, [a, b ,c]]
# new_list = datos[4]


# print(datos[4][1])
# print(new_list[1])


equipos_futbol = ["CaracasFC", "Mineros", "LaraFC"]
# print(equipos_futbol)

# Agregando elementos -> append
equipos_futbol.append(["DeportivoTachira", "Barca"])
# print(equipos_futbol)

# Quitar elementos -> pop
equipos_futbol.pop(1)
# print(equipos_futbol)

equipos_futbol[2].pop(0)
# print(equipos_futbol)

# Tuplas -> tuple -> colecciones de datos -> ()
# Las tuplas (tuple) -> son inmutables

datos_nombres = ("Carlos", "Hendrik", "Jose")

print(type(datos_nombres))
print(datos_nombres[0])

#!datos_nombres.append("Adrian")
#!datos_nombres.pop(0)
print(datos_nombres)