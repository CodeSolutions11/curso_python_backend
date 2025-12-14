from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipo, Seguidor, Comentario
from django.http import JsonResponse

def home(request):
    equipos_top = sorted(Equipo.objects.all(), key=lambda x: x.puntos, reverse=True)[:3]
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos_top})

def lista_equipos(request):
    liga = request.GET.get('liga', '')  
    equipos = sorted(Equipo.objects.all(), key=lambda x: x.puntos, reverse=True)
    if liga:
        equipos = equipos.filter(liga=liga)
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})
    
def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    comentarios = Comentario.objects.filter(equipo=equipo)[:5]
    es_seguidor = False
    if request.user.is_authenticated:
        es_seguidor = Seguidor.objects.filter(usuario=request.user, equipo=equipo).exists()
    return render(request, 'equipos/detalle_equipo.html', {
        'equipo': equipo,
        'comentarios': comentarios,
        'es_seguidor': es_seguidor
    })


@login_required
def toggle_seguidor(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    seguidor, creado = Seguidor.objects.get_or_create(usuario=request.user, equipo=equipo)
    if not creado:
        seguidor.delete()
        return JsonResponse({'siguiendo': False})
    return JsonResponse({'siguiendo': True})    

@login_required
def agregar_comentario(request, id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=id)
        mensaje = request.POST.get('mensaje', '')
        if mensaje:
            Comentario.objects.create(usuario=request.user, equipo=equipo, mensaje=mensaje)
        return redirect('detalle_equipo', id=id)