import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from EdbooksApp.models import Libro

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
    #GET
    if request.method == "GET":
        return render(request, "formulario_libro.html", {})

    #POST
    if request.method == "POST":
        info_formulario = request.POST
        libro = Libro(info_formulario["titulo"], info_formulario["autor"], info_formulario["año"])
        libro.save()
        return render(request, "formulario_libro.html", {})
