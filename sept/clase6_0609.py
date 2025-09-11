def operacion(param1, param2, type):
    if type == "suma":
        return param1 + param2
    elif type == "resta":
        return param1 - param2
    elif type == "multiplicar":
        return param1 * param2
    elif type == "dividir":
        return param1 / param2
    else:
        return "error al ejecutar la operación"

typesOperations = ["suma", "resta", "multiplicar", "dividir"]
# print(typesOperations[4]) # ! Error

# print(operacion(7, 10, typesOperations[0]))
# print(operacion(7, 10, typesOperations[1]))
# print(operacion(7, 10, typesOperations[2]))
# print(operacion(7, 10, typesOperations[3]))
# print(operacion(7, 10, ""))


# TODO: Argumentos por palabra clave (Keyword Arguments)
def createProfile(name, age, city, profession):
    return {
        "name": name,
        "age": age,
        "city": city,
        "profession": profession
    }

# Usando keywords - el orden no importa

profile = createProfile(
    profession ="Ingeniero",
    name = "Jesus",
    city = "Caracas",
    age = 25
)
# print(profile)

profile2 = createProfile("José", age = 30, city="Bqsto", profession="Doctor")

# print(profile2)


# Argumentos por defecto
def saludarConTitulo(name, title="Sr./Sra."):
    return f"Hola, {title} {name}"

# print(saludarConTitulo("Moreno"))
# print(saludarConTitulo("Moreno", "Ing."))

# ! OJITOO! - Valores mutables por defecto
def agregarItem(item, lista=[]):
    lista.append(item)
    return lista

# Problema: la lista se reutiliza
# print(agregarItem("a"))
# print(agregarItem("b")) # No esperado - ["a", "b"]

# Todo: Lo correcto sería
def agregarItemCorrecto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

# print(agregarItemCorrecto("X"))
# print(agregarItemCorrecto("O"))
# print(agregarItemCorrecto("Z", ["A", "B"]))

# Todo: *args - Argumentos Variables Posicionales
def sumarTodos(*nros):
    print(nros)
    total = 0
    for nro in nros:
        total += nro #total = total + nro
    return total

# print(sumarTodos(1, 2, 3))
# print(sumarTodos(10, 2, 3))

def procesarDatos(operation, *valores):
    if operation == "suma":
        return sum(valores)
    elif operation == "producto":
        resultado = 1
        for valor in valores:
            resultado *= valor
        return resultado
    else:
        return "Operación no válida"

# print(procesarDatos("suma", 1, 2, 3, 4))
# print(procesarDatos("producto", 2, 5, 4))


# **kwargs - Argumentos Variables por Palabra Clave
def createUser(**datos):
    # datos es un diccionario
    user = {}
    for clave, valor in datos.items():
        user[clave] = valor
    return user

user1 = createUser(name="Cesar", age=25, city="Maracay")
user2 = createUser(tel="04241112233", dir="Css", city="Maracay")

# print(user1)
# print(user2)

# Todo: combinar *args y **kwargs
def funcionCompleta(req, porDefecto="default", *args, **kwargs):
    print(f"Requerido: {req}")
    print(f"Por defecto: {porDefecto}")
    print(f"Args adicionales: {args}")
    print(f"Kwargs: {kwargs}")

# funcionCompleta("value1", "val2", "extra1", "extra2", clave="value", clave2="other")

# Todo: Ejercicio Práctico: Sistema de Calculadora

    ## Calculadora flexible que acepta múltiples nros
    #Args: 
    #    operacion (str): tipo de operacion ('suma', 'resta', 'multiplicacion', 'division')
    # precision (int): decimales a mostrar
    # mostrarProceso (bool): Si mostrar el proceso de cálculo
    # Returns:
        # float: Resultado de la operacion

def calculadora(operacion, *numeros, precision=2, mostrarProceso=False):
    if not numeros:
        return "Error: Se necesita al menos un número"

    if operacion == "suma":
        result = sum(numeros)
        if mostrarProceso:
            print(f"Sumando: {"+".join(map(str, numeros))} = {result}")

    elif operacion == "resta":
        result = numeros[0]
        for num in numeros[1:]:
            result -= num
        if mostrarProceso:
            print(f"Restando: {numeros[0]} - {"-".join(map(str, numeros[1:]))} = {result}")

    elif operacion == "division": 
        if 0 in numeros[1:]:
            return "Error: división por cero"
        result = numeros[0]
        

    return round(result, precision)

# print(round(17, 3))
print(calculadora("suma", 1, 20, 3, 4, 5, mostrarProceso=True))
print(calculadora("resta", 10, 2, 3, 4, 5, mostrarProceso=True))
