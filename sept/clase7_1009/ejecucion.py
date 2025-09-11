
# TODO: 1. Importar módulo completo
import matematicas

#print(matematicas)

result = matematicas.sumar(5, 10)
print(result)

# TODO: 2. Importar funciones específicas
from matematicas import restar, sumar

print(restar(17, 15))
print(sumar(17, 15))

# multiplicar = 7
# matematicas = 25

# TODO: 3. Importar con alias
import matematicas as math
from matematicas import multiplicar as mult

print(math.multiplicar(2, 5))
print(mult(5, 5))

import test
test.testing()