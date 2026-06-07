from django.shortcuts import render
from .models import ContenidoAudiovisual

# Create your views here.
def inicio_materias (request):
    return render(request, 'inicio.html')

def ver_materia(request, anio):
    videos = ContenidoAudiovisual.objects.filter(anio=anio)

    if anio== '2':
        nombre_materia = 'Segundo Año'
    else:
        nombre_materia = 'Cuarto Año'

    contexto = {
        'videos': videos,
        'nombre_materia': nombre_materia,
    }
    return render(request, 'materia.html', contexto)