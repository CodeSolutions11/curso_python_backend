nameFile = "test.txt"
with open(nameFile, "a") as archivo:
    archivo.write("\nLínea 4: Contenido añadido")

# Verificar el Contenido
with open(nameFile, "r") as archivo:
    print("Contenido después de añadir")
    print(archivo.read())

# Modo escritura con encoding
datosNuevos = ["Producto: Laptop", "Precio: $800", "Stock: 15"]

with open("inventario.txt", "w", encoding="utf-8") as archivo:
    for dato in datosNuevos:
        archivo.write(dato + "\n")

print("Archivo de inventario creado")
