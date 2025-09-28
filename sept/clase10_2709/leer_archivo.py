def leerArchivoCompleto(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r") 
        contenido = archivo.read()
    except FileNotFoundError:
        print(f"Archivo: '{nombre_archivo} no encontrado'")
    else:
        print("Archivo leído exitosamente")
        return contenido
    finally:
        try:
            archivo.close()
            print("Archivo cerrado")
        except:
            pass


# Crear archivo de prueba y ejecutar 
with open("test.txt", "w") as f:
    f.write("Contenido de prueba")

result = leerArchivoCompleto("./example_division_segura.py")
print(f"Contenido: {result}")
