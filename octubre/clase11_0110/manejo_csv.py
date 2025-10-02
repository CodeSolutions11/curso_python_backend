import csv 

datosEmpleados = [
    ["Nombre", "Edad", "Departamento", "Salario"],
    ["Cesar", 25, "IT", 50000],
    ["Andrea", 22, "Marketing", 25],
    ["Jose", 35, "Ventas", 1500]
]

# Crear archivo CSV 
with open("empleados.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datosEmpleados)

# Leer archivo CSV
print("Datos de empleado:")
with open("empleados.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for row in lector:
        print(row)
