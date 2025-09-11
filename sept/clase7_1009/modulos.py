
# TODO: Módulos del sistema
import os
import sys
import datetime
import random
import json

# Información del sistema
print(os)
print(f"Sistema operativo: {os.name}")
print(f"Directorio actual: {os.getcwd()}")
print(f"Versión Python: {sys.version}")

# Fecha y hora
ahora = datetime.datetime.now()
print(f"Fecha actual: {ahora.strftime('%y-%m-%d %H:%M')}")

# Números aleatorios
nro_aleatorio = random.randint(1, 100)
print(f"Número aleatorio: {nro_aleatorio}")


# JSON
datos = {"nombre": "Jesus", "edad": 28}
print(datos, type(datos))
json_string = json.dumps(datos)
print(json_string, type(json_string))

## Paquetes
    # mi_paquete/
        #__init__.py
        # modulo1.py
        # modulo2.py
        # subpaquete/
            # __init__.py
            # modulo3.py