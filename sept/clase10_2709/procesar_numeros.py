# Múltiples excepciones
def procesarNumeros(texto):
    try:
        numero = int(texto)
        result = 100/numero
        print(result)
    except ValueError:
        print(f"'{texto}' es un numero no válido  ")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except Exception as e:
        print(f"Error inesperado: {e}")


procesarNumeros("10")
procesarNumeros("abc")
procesarNumeros("0")
print(procesarNumeros("0"))
