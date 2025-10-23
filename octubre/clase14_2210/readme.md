## Pasos para crear un proyecto con django

```bash
# Crear entorno virtual
python3 -m venv django_env

# Activar entorno virtual
source django_env/bin/acttivate # Linux
django_env/Scripts/acttivate

# Instalar Django
pip3 install django

# Verificar instalación
python3 -m django --version

# Crear proyecto
django-admin startproject project_class_14

# Crear base de datos inicial
python3 manage.py migrate

# Crear superusuario para el admin
python3 manage.py createsuperuser

# Levantar/correr proyecto
python3 manage.py runserver
```

## Qué es una "App" en Django

Una app es como un "módulo funcional" de tu sitio web. Piénselo así:

```
PROYECTO = Edificio completo
|-- App "tienda" = Planta baja (productos, ventas)
|-- App "blog" = Primer piso (artículos, comentarios)
|-- App "usuarios" = Segundo piso (perfiles, auth)
|-- App "contacto" = Recepción (formularios, mensajes)
```

### Filosofía de Django: "Una app, una Función"

```python
# Bien: Apps específicas
blog/     # Solo para artículos y comentarios
tienda/   # Solo para productos y ventas
usuarios/ # Solo para perfiles y autenticación

# Mal: App que hace todo
sitio_web/  # Mezcla blog, tienda, usuarios, etc...
```

## Estructura de una App en Django

```
mi_app/
  |-- __init__.py   # Hace que sea un paquete de python
  |-- admin.py      # Config del panel admin
  |-- apps.py       # Config de la app
  |-- models-py     # Modelos de datos (base de datos)
  |-- views.py      # lógica de las páginas
  |-- test.py       # Pruebas automatizadas
  |-- urls.py       # Rutas específicas de la app (no existe por defecto)
  |-- migrations/   # Cambios en la base de datos
          |-- __init__
```

## Crear una app

```bash
#Crear app
python3 manage.py startapp blog
```
