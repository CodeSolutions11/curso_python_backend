## Qué es un ORM??

ORM = Object-Relational Mapper. Es como es un "traductor" entre python y la base de datos

- **Sin ORM**: Escribiria SQL manualmente (`SELECT * FROM users WHERE edad > 18`)
- **Con ORM**: Usas Python (`User.objects.filter(edad__get=18)`)

## **Flujo de trabajo con Modelos**

```
1. Crear/Modificar modelo -> 2. makemigrations -> 3. migrate -> 4. Usar modelo
    (models.py)                 (crear archivo)     (aplicar)     (views.py)
```
