### DJANGO

### Conceptos Clave

## Django Framework

- **Framework "betteries included"**: Incluye todo lo necesario para desarrollo web
- **MVT (Model-view-Template)**: Patrón arquitectónico de DJANGO
- **ORM**: Mapeo objeto-relacional para bases de datos
- **Admin Interface**: Panel de administración automático

## Estructura del proyecto

- **manage.py**: Script de gestión del proyecto
- **settings.py**: Configuración del proyecto
- **urls.py**: Erutamiento de urls
- **wsgi.py/asgi.py**: Interfaces para servidores web

## Aplicaciones Django

- **App**
- models.py
- **views.py**
- **urls.py**

### Instalación de Django

```bash
# Crear entorno visual
python3 -m venv django_env

# Activar el entorno visual (Linux/Mac)
source django_env/bin/activate
# Activar el entorno visual (windows)
django_env/Scripts/activate
```

### Instalar Django

```bash
pip install django

python3 -m django --version # Verificar
```

### Crear proyecto

```bash
django-admin startproject my_first_project

cd my_first_project
```

### Ejecutar servidor de desarrollo

```bash

python3 manage.py runserver ## Por defecto en el puerto 8000
pyhton3 manage.py runserver 8001 ## usa un puerto especifico (8001 en este caso )

python3 manage.py makemigrations # Crear migraciones
python3 manage.py migrate # Aplicar migraciones
python3 manage.py createsuperuser # Crear superusuario
```
