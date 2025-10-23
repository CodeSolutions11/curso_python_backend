from django.contrib import admin
from django.urls import path, include 
from django.http import HttpResponse

# Crear una vista simple 
def inicio(request):
    return HttpResponse("""
        <h1 style="color:red;"> Mi primer sitio Django </h1>
        <p>Esto funciona perfectamente</p>
        <a style="background:blue; color:white; padding: 10px 3rem;" href="/blog/">Mi blog</a>
        <a style="background:black; color:white; padding: 10px 3rem;" href="/admin/">Ir al panel de administrador</a>
    """)

urlpatterns=[
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("blog/", include('blog.urls')), # Incluir URLs del blog
]
