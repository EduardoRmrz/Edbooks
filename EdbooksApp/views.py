import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, Template

from EdbooksApp.models import Autores, Libro
from .forms import *
from django.db.models import Q


# Create your views here.
def inicio(request):
    hoy = datetime.datetime.now()
    return render(request, "index.html", {"dia_hora":hoy})

def libros(request):

    # return HttpResponse("Vista de libros")
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            libros = Libro.objects.filter( Q(titulo__icontains=search) | Q(autor__icontains=search) ).values()
            return render(request, "libros.html", {"libros":libros, "search":True, "busqueda":search})

    libros = Libro.objects.all()
    return render(request, "libros.html", {"libros":libros})

def usuarios(request):
    return HttpResponse("Vista de usuarios")

def autor(request):
    #return HttpResponse("Vista de autores")
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            autores = Autores.objects.filter( Q(nombre__icontains=search) | Q(nacionalidad__icontains=search) ).values()
            return render(request, "autores.html", {"autores":autores, "search":True, "busqueda":search})
    autores = Autores.objects.all()
    return render(request, "autores.html", {"autores":autores})

def crear_autor(request):
    #POST
    if request.method == "POST":
        formulario = NuevoAutor(request.POST)
        if formulario.is_valid():
            info_autor = formulario.cleaned_data
            autor = Autores(nombre=info_autor["nombre"], apellido=info_autor["apellido"], nacionalidad=info_autor["nacionalidad"])
            autor.save()
            return redirect("autores")
        else:
            redirect("crear_autor")

    #GET Y OTROS METODOS
    else:
        formulariovacio = NuevoAutor()
        return render(request, "formulario_autor.html", {"form":formulariovacio})

def buscar_autor(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        nombres = Autores.objects.filter(nombre__icontains=nombre)
        return render(request, "busqueda_autor.html", {"nombres":nombres})
    else:
        nombres = []
        return render(request, "busqueda_autor.html", {"nombres":nombres})

def eliminar_autor(request, autor_id):
    autor = Autores.objects.get(id=autor_id)
    autor.delete()
    return redirect("autores")


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
    if request.method == "POST":
        titulo = request.POST["titulo"]
        titulos = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, "busqueda_libro.html", {"titulos":titulos})
    else:
        titulos = []
        return render(request, "busqueda_libro.html", {"titulos":titulos})

def eliminar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    libro.delete()
    return redirect("libros")

# def editar_libro(request, libro_id):
#     libro = Libro.objects.get(id=libro_id)

#     #GET Y OTROS METODOS
#     else:
#         formulariovacio = NuevoLibro()
#         return render(request, "formulario_libro.html", {"form":formulariovacio})
