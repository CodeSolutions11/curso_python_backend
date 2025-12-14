from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    path('seguir/<int:id>/', views.toggle_seguidor, name='toggle_seguidor'),
    path('comentar/<int:id>', views.agregar_comentario, name='agregar_comentario'),
]
         