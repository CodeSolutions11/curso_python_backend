### Diccionarios -> dict -> {}
# Estructura clave-valor (JSON)
# Fundamentales para APIs REST
# Representación de objetos y datos estructurados

# Crear un diccionario clave-valor (JSON)
#print("Creando un diccionario")

usuario_perfil = {
    "id": 1,
    "nombre": "Jesus",
    "edad": 28,
    "activo": True,
    "roles": ["admin", "user", "profesor"],
    "ultimo_login": "2025-08-24T10:30:00z"
}

# print(f"Perfil de usuario: {usuario_perfil}")
# print(f"Tipo de dato: {type(usuario_perfil)}")
# print(f"Nombre: {usuario_perfil['nombre']}")
#print(f"Email: {usuario_perfil["email"]}")

# print(f"Email: {usuario_perfil.get("email", "No disponible")}")
# print(f"Role: {usuario_perfil["roles"][1]}")
# print(f"Lista roles: {usuario_perfil["roles"]}")
# print(f"Roles: {' - '.join(usuario_perfil["roles"])}")

# Agregar nueva info
usuario_perfil["fecha_registro"] = "2025-08-01"
usuario_perfil["intentos_login"] = 0
#print(f"Perfil actualizado: {usuario_perfil}")


## Simular respuesta de una API

response_api = {
    "status": "success",
    "data": usuario_perfil,
    "message": "Usuario encontrado",
    "timestamp": "2025-08-24T10:30:00z"
}

print(f"Respuesta API: {response_api}")