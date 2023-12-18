from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def docentes(request):
    return render(request, 'docentes.html')

def crear_docente(request):
    return render(request, 'crear_docente.html')

def cursos(request):
    return render(request, 'cursos.html')

def crear_curso(request):
    return render(request, 'crear_curso.html')