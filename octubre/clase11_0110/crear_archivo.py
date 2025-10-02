contenidoInicial = """Línea 1: Datos importante
Línea 2: Más informacion
Línea 3: Final del archivo"""

# Modo de escritura ("w") - Sobrescribe el archivo
with open("test.txt", "w") as archivo:
    archivo.write(contenidoInicial)
print("Archivo creado exitosamente!!")
