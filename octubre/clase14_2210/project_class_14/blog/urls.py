from django.urls import path 
from . import views

# Nombre de la app para evitar conflictos

app_name = "blog"

urlpatterns = [
    path("", views.inicio_blog, name="inicio"),
    path("articulo/<int:numero_articulo>/", views.ver_articulo, name="articulo"),
    path("todos/", views.lista_articulos, name="todos"),
]
