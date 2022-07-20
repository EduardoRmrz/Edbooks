import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, Template

from EdbooksApp.models import Libro
from .forms import *

# Create your views here.
def inicio(request):
    hoy = datetime.datetime.now()
    return render(request, "index.html", {"dia_hora":hoy})

def libros(request):
    # return HttpResponse("Vista de libros")
    libros = Libro.objects.all()
    return render(request, "libros.html", {"libros":libros})

def usuarios(request):
    return HttpResponse("Vista de usuarios")

def autor(request):
    #return HttpResponse("Vista de autores")
    return render(request, "autores.html", {})

def about(request):
    # return HttpResponse("Vista de about")
    return render(request, "about.html", {})

def base(request):
    return render(request, "base.html", {})

def crear_libro(request):
    #POST
    if request.method == "POST":
        formulario = NuevoLibro(request.POST)
        if formulario.is_valid():
            info_libro = formulario.cleaned_data
            libro = Libro(titulo=info_libro["titulo"], autor=info_libro["autor"], año=int(info_libro["año"]))
            libro.save()
            return redirect("libros")
        else:
            redirect("crear_libro")

    #GET Y OTROS METODOS
    else:
        formulariovacio = NuevoLibro()
        return render(request, "formulario_libro.html", {"form":formulariovacio})

def buscar_libro(request):
    titulos = []
    return render(request, "busqueda_libro.html", {"titulos":titulos})
    
