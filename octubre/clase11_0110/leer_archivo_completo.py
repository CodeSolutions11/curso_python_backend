nameFile = "calculadora.py"

try:
    with open(nameFile, "r") as archivo:
        # Leer todo el contenido
        contenidoCompleto = archivo.read()
        print("Contenido completo:")
        print(contenidoCompleto)
        print("-" * 30)

    # Leer línea por línea
    with open(nameFile, "r") as archivo:
        print("Línea por línea:")
        for numberLine, line in enumerate(archivo, 1):
            print(f"{numberLine}: {line.strip()}")
except FileNotFoundError:
    print("Archivo no encontrado")

