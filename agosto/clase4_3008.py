# Convenciones para nombrar variables
# camelCase = "camelCase"
# snake_case = "snake_case"
# PascalCase = "PascalCase"


## SETS -> Colecciones únicas
### Utilidad: permisos, tags, filtros
permisos_usuarios = {"lectura", "escribir", "actualizar","eliminar"}
permisos_invitado = {"lectura"}
ips_bloqueadas = {"192.168.1.100", "10.0.0.50", "172.16.0.25"}

# print(f"Permisos de usuario: {permisos_usuarios}")
# print(f"Permisos de invitado: {permisos_invitado}")

# Operaciones con sets
permisos_extras = permisos_usuarios - permisos_invitado
#print(f"Permisos extras del usuario: {permisos_extras}")

# Verificar permisos
ip_cliente = "192.168.1.107"
acceso_permitido = ip_cliente not in ips_bloqueadas
#print(f"IP {ip_cliente} puede acceder: {acceso_permitido}")

### Operadores -> Operadores aritmeticos - Operadores de comparación - Operadores lógicos

# Operadores aritmeticos: suma, resta, multiplicación, división, modulo, potencia
# Cálculos típicos del backend

precio_base = 1000.00 #float
impuesto = 0.16 # float
descuento = 0.10 # float 
cantidad = 3 # int

subtotal = precio_base * cantidad
descuento_aplicado = subtotal * descuento
base_imponible = subtotal - descuento_aplicado
impuesto_aplicado = base_imponible * impuesto
total = base_imponible + impuesto_aplicado

# print(f"Subtotal: {subtotal} bs")
# print(f"Descuento aplicado: {descuento_aplicado} bs")
# print(f"Base imponible: {base_imponible} bs")
# print(f"Impuesto aplicado: {impuesto_aplicado} bs")
# print(f"Total a pagar: {total} bs")

a = 12
b = 2
# print(f"División: {a} / {b} = {a / b}")
# print(f"Módulo -> Resto: {a} % {b} = {a % b}") # Resto de una division
# print(f"Potencia: {a} ** {b} = {a ** b}") # Potencia)

# Operadores de comparación: Igualdad ==, Desigualdad !=, Mayor qué >, Menor qué <, Mayor o igual >=, Menor o igual <=

# SI => True - NO => False

# Validaciones típicas
edad_usuario = 20
edad_minima = 18
saldo_cuenta = 1500.00
monto_compra = 2500.00

puede_registrarse = edad_usuario >= edad_minima  

print(f"Edad del usuario: {edad_usuario} ¿Puede registrarse? {puede_registrarse}")

tiene_saldo_suficiente = saldo_cuenta >= monto_compra
print(f"Saldo en cuenta: {saldo_cuenta} ¿Puede comprar? {tiene_saldo_suficiente}")

c = 10
d = 10
# print(f"Igualdad: si {c} == {d}: {c == d}")
# print(f"Desigualdad: si {c} != {d}: {c != d}")
# print(f"Mayor qué: si {c} > {d}: {c > d}")
# print(f"Mayor ó igual: si {c} >= {d}: {c >= d}")


## Operadores lógicos: and, or, not
# Combinación de condiciones típicas

# print(f"AND: { 3 < 5 and 15 <= 20 and 30 <= 15 and 15 <= 15 and 15 <= 15 and 15 <= 15 and 150 <= 15 and 15 <= 15}")
# print(f"AND: { 10 == 10 and 11 != 11}")

# print(f"OR: { False or False or True or False}")
# print(f"OR: { 10 == 10 or 11 != 11}")

# print(f"NOT: { not True }")
# print(f"NOT: { not False }")

# print(f"NOT: not (10 == 10):  { not (10 == 10) }")

tiene_email = True
acepta_terminos = True
mayor_edad = True
email_verificado = False

puede_crear_cuenta = tiene_email and acepta_terminos and mayor_edad
necesita_verificar_email = not email_verificado 
acceso_completo = puede_crear_cuenta and not necesita_verificar_email

print(f"¿Puede crear cuenta? {puede_crear_cuenta}")
print(f"¿Necesita verificar email? {necesita_verificar_email}")
print(f"¿Acceso completo? {acceso_completo}")