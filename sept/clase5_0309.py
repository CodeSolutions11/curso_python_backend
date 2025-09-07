### Estructuras de control

# Condiconales  -> if/else

edad = 18
# tab
# if edad < 18:
#     mensaje = { "valido": False, "mensaje": "Debe ser mayor a 18 años" }
#     print(f"{mensaje}")
# else:
#     mensaje = { "valido": True, "mensaje": "Usuario valido para el registro" }
#     print(f"{mensaje}")

## if/else - elif
# if edad < 18:
#     mensaje = { "valido": False, "mensaje": "Debe ser mayor a 18 años" }
#     print(f"{mensaje}")
# elif edad == 18:
#     mensaje = { "valido": True, "mensaje": "Acceso limitado" }
#     print(f"{mensaje}")
# else: 
#     mensaje = { "valido": True, "mensaje": "Usuario valido para el registro" }
#     print(f"{mensaje}")

user = {
    "name": "Jesus",
    "email": "jesus@gmail.com",
    "plan": "plata"
}
planes = [ "plata", "oro", "diamante" ]


# if user["email"] == "jesus@gmail.com" and user["plan"] == planes[0]: 
#     print(f"Usuario logueado con el plan {planes[0]}")

# elif user["email"] == "jesus@gmail.com" and user["plan"] == planes[1]:
#     print(f"Usuario logueado con el plan {planes[1]}")

# elif user["email"] == "jesus@gmail.com" and user["plan"] == planes[2]:
#     print(f"Usuario logueado con el plan {planes[2]}")
# else:
#     print("Usuario no existe")


# if 2 * 7 == 15:
#     print(f"el resultado de 2 *  7 == 15 es: {2 *  7 == 15}")

# elif not(17%2 != 0):
#     print(f"El resultado de not(17%2 != 0) es: {not(17%2 != 0)}")

# else:
#     print("Toda las condiciones son falsas")

## Funciones -> def
# Definición de una función básica
def saludar():
    print("Hola Mundo!!")

# llamada a la función
saludar()

## Función con parámetros
def saludarPersona(name):
    print(f"Holaa {name}")

# saludarPersona("Adrian")
# saludarPersona("José")
# saludarPersona("César")

## Función con valor de retorno
def sumar(a, b):
    return a + b

result = sumar(7, 9)
result2 = sumar(17, 9)
result3 = sumar(25, 19)

# print(type(sumar))
# print(type(result))
# print(result2)
# print(result3)

### len() -> me retorna la cantidad carácteres que tiene una variable
# password = "abc123"
# print(len(password))

def validarRegistroUsuario(edad, email, passwd):
    # Valida los datos de registro de un usuario
    if edad < 18:
        return { "valido": False, "mensaje": "Debe ser mayor a 18 años" }
    elif "@" not in email or "." not in email:
        return { "valido": False, "mensaje": "Email no es válido"}
    elif len(passwd) < 8:
        return { "valido": False, "mensaje": "Password debe tener al menos 8 caracteres"}
    else:
        return { "valido": True, "mensaje": "Usuario válido para registro"}   


usuarios = [
    {"edad": 17, "email": "user@gmail.com", "passwd": "abc123456"},
    {"edad": 27, "email": "user@gmailcom", "passwd": "abc123456"},
    {"edad": 17, "email": "user@gmail.com", "passwd": "abc123456"},
    {"edad": 35, "email": "user@gmail.com", "passwd": "abc12"},
    {"edad": 20, "email": "user@gmail.com", "passwd": "shasdgkjdffdikgjfd"},
]
# print(usuarios[4]["edad"], usuarios[4]["email"], usuarios[4]["passwd"])

# print(validarRegistroUsuario(usuarios[4]["edad"], usuarios[4]["email"], usuarios[4]["passwd"]))

# print(validarRegistroUsuario(usuarios[1]["edad"], usuarios[1]["email"], usuarios[1]["passwd"]))

# print(validarRegistroUsuario(usuarios[3]["edad"], usuarios[3]["email"], usuarios[3]["passwd"]))




### Bucle For

nros = [ 1, 15, 23, 30 ]

#print(nros)

for x in nros:
    print(x)

# print(nros, type(nros))

datos = [
    ("laptop", "30000 bs", False),
    ("tv", "45000 bs", True),
]

for product in datos:
    print(product)

nombres = [("jesus", 25)]
## destructuring de tuplas
name, edad = nombres[0]
## name = nombres[0][0]
## edad = nombres[0][1]
# print(name, edad)



def validarRegistroUsuario2(edad, email, passwd):
    # Valida los datos de registro de un usuario
    if edad < 18:
        return { "valido": False, "mensaje": "Debe ser mayor a 18 años" }
    elif "@" not in email or "." not in email:
        return { "valido": False, "mensaje": "Email no es válido"}
    elif len(passwd) < 8:
        return { "valido": False, "mensaje": "Password debe tener al menos 8 caracteres"}
    else:
        return { "valido": True, "mensaje": "Usuario válido para registro"}   


casos_prueba = [
    (15, "jesus@gmail.com", "12345678"),
    (25, "user@gmail.com", "12345678"),
    (28, "user2@gmail.com", "123"),
    (30, "user3@gmail.com", "passwd123"),
]

for edad, email, passwd in casos_prueba:
    result = validarRegistroUsuario2(edad, email, passwd)
    print(f"Usuario({edad}, '{email}', '{passwd}'): {result["mensaje"]}")



