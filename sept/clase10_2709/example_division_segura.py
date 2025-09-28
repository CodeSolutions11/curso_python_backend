def divisionSegura(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None
        
# Prueba 
division1 = divisionSegura(10, 2)
print(division1)

division2 = divisionSegura(10, 0)
print(division2)


