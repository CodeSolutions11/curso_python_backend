from django.shortcuts import render
from django.http import HttpResponse


def inicio_blog(request):
    """ Vista principal del blog """
    html = """
        <h1>Bienvenido a mi Blog!!</h1>
        <p>Este es mi primer blog hecho con Django </p>
        <ul>
            <li><a href="/blog/articulo/1/">Mi primer aritculo</a></li>
            <li><a href="/blog/articulo/2/">Aprendiendo Django</a></li>
            <li><a href="/blog/articulo/3/">Django es interesante</a></li>
        </ul>
        <p><a href="/">Volver al inicio </a></p>
    """
    return HttpResponse(html)


def ver_articulo(request, numero_articulo):
    """ Vista de artículos independientes """
    # Simular una base de datos con un diccionario
    articulos = {
        1: {
            'titulo': 'Mi primer articulo',
            'contenido': "Este es mi primer artículo en Django.",
            'autor': "JesusDev"
        },
        2: {
            'titulo': 'Aprendiendo Django',
            'contenido': "Django es increible, hace que crear sitios webs sea muy fácil.",
            'autor': "JesusDev"
        },
        3: {

            'titulo': 'Django es interesante',
            'contenido': "Django es el mejor framework de python para backend.",
            'autor': "JesusDev"
        },
    }


    # Buscar el artículo 
    if numero_articulo in articulos:
        articulo = articulos[numero_articulo]
        html = f"""
        <h1> {articulo['titulo']}</h1>
        <p><strong>Por: </strong>{articulo['autor']}<p>
        <hr>
        <a href="/blog/">Volver al blog</a>
        """
    else:
        html = """
        <h1>Artículo no encontrado</h1>
        <p>El artículo que buscas no existe</p>
        <a href="/blog/">Volver al blog</a>
        """

    return HttpResponse(html)


def lista_articulos(request):
    """ Vista que muestra todos los artículos"""
    articulos = [
        {'id': 1, 'titulo': 'Mi primer artículo', 'resumen': 'Una introducción a mi blog'},
        {'id': 2, 'titulo': 'Aprendiendo Django', 'resumen': 'Mis primeros pasos con django'},
        {'id': 3, 'titulo': 'Django es interesante', 'resumen': 'Por qué django es interesante'},
    ]

    html = "<h1>Todos los Artículos</h1>"

    for articulo in articulos: 
        html += f"""
        <div style="border: 1px solid #ccc; margin: 10px; padding:10px;">
            <h3><a href="/blog/articulo/{articulo['id']}/">{articulo[titulo]}</a></h3>
            <p>{articulo['resumen']}</p>
        """
    html += "<p><a href='/blog/'> volver al blog</a></p>"

    return HttpResponse(html)
