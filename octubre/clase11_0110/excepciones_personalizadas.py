# Definir excepciones propias
#

class EdadInvalidaError(Exception):
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validarEdad(edad):
    if edad < 0:
        raise EdadInvalidaError(edad, "La edad no puede ser negativa")
    if edad > 110:
        raise EdadInvalidaError(edad, "La edad no puede ser mayor a 110")
    return True

# Pruebas 

try: 
    validarEdad(-5)
except EdadInvalidaError as e:
    print(f"Error: {e.mensaje}, edad recibida: {e.edad}")

try:
    validarEdad(125)
except EdadInvalidaError as e:
    print(f"Error: {e.mensaje}, edad recibida: {e.edad}")
