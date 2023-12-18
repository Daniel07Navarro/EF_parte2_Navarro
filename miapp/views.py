from django.shortcuts import render
from miapp.models import Docente
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def crear_docente(request):
    return render(request, 'crear_docente.html')

def guardar_docente(request):
    if request.method == 'GET':
        codigo = request.GET['codigo']
        nombre = request.GET['nombre']
        apellido_paterno = request.GET['apellido_paterno']
        apellido_materno = request.GET['apellido_materno']
        dni = request.GET['dni']
        fecha_nacimiento = request.GET['fecha_nacimiento']
        estado = request.GET['estado']
    docente = Docente(
        codigo = codigo,
        nombre = nombre,
        apellido_paterno = apellido_paterno,
        apellido_materno = apellido_materno,
        dni = dni,
        fecha_nacimiento = fecha_nacimiento,
        fecha_registro = str(datetime.now()),
        estado = estado
    )
    docente.save()
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def eliminar_docente(request,iddocente):
    docente=Docente.objects.get(iddocente=iddocente)
    docente.delete()
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def cursos(request):
    return render(request, 'cursos.html')

def crear_curso(request):
    return render(request, 'crear_curso.html')