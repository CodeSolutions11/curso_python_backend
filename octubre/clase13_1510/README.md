FRAMEWORK - DJANGO

sin django -> Tendriamos que hacer los ladrillos, mezclar el cemento, crear
las herramientas, etc...

Con Django -> Me da todos los materiales y herramientas listas para usar

Patron MVT (model - view - template)

Model VIEW TEMPLATE
(datos) lógica (HTML)
Base de python code Presentación
datos

Qué incluye Django automáticamente??

- Sistema de usuarios y autenticación
- Panel de administración web
- Manejo de bases de datos (ORM)
- Sistema de plantillas HTML
- Seguridad contra ataques web
- Manejo de formularios
- Sistema de archivos estáticos (CSS, JS, imágenes)
- Internacionalización (múltiples idiomas)

Crear entorno virtual - Muy importante!!

- Evita conflictos entre proyectos
- Mantiene versiones específicas
- Facilita el despliegue

Crear entorno virtual
python3 -m venv django_env -> (puede ser cualquier nombre)

Activar entorno en windows
django_env/Scripts/activate

Instalación de django
pip3 install django

Verificar instalación
python3 -m django --version

Crear base de datos inicial (Ejecutar migracion)
python3 manage.py migrate

Crear superusuario
python3 manage.py createsuperuser

Ejecutar servidor
python3 manage.py runserver
-> localhost:8000 #(Tu pagina personalizada)
-> localhost:8000/admin #(Panel administrativo)
