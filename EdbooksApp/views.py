import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, Template

from EdbooksApp.models import Autores, Avatar, Lector, Libro
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def inicio(request):
    hoy = datetime.datetime.now()

    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url =  "/media/avatar/generica.png" 
        return render(request, "index.html", {"dia_hora":hoy, "url":url})
    
    return render(request, "index.html", {"dia_hora":hoy})

def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request, "login.html",{"form":form})

def register_request(request):
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            form.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"register.html",{"form":form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request,"register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def libros(request):

    # return HttpResponse("Vista de libros")
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            libros = Libro.objects.filter( Q(titulo__icontains=search) | Q(autor__icontains=search) ).values()
            return render(request, "libros.html", {"libros":libros, "search":True, "busqueda":search})

    libros = Libro.objects.all()
    return render(request, "libros.html", {"libros":libros})

@staff_member_required
def lectores(request):
    return render(request, 'lectores.html',{})

@login_required
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

def editar_autor(request, autor_id):
    autor = Autores.objects.get(id=autor_id)
    if request.method == "POST":
        formulario = NuevoAutor(request.POST)
        if formulario.is_valid():
            info_autor = formulario.cleaned_data
            autor.nombre = info_autor["nombre"]
            autor.apellido = info_autor["apellido"]
            autor.nacionalidad = info_autor["nacionalidad"]
            autor.save()
            return redirect("autores")


    #GET Y OTROS METODOS
    formulario = NuevoAutor(initial={"nombre":autor.nombre, "apellido":autor.apellido, "nacionalidad":autor.nacionalidad})
    return render(request,"formulario_autor.html",{"form":formulario})

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

def editar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    if request.method == "POST":
        formulario = NuevoLibro(request.POST)
        if formulario.is_valid():
            info_libro = formulario.cleaned_data
            libro.titulo = info_libro["titulo"]
            libro.autor = info_libro["autor"]
            libro.año = info_libro["año"]
            libro.save()
            return redirect("libros")


    #GET Y OTROS METODOS
    formulario = NuevoLibro(initial={"titulo":libro.titulo, "autor":libro.autor, "año":libro.año})
    return render(request,"formulario_libro.html",{"form":formulario})

@login_required
def editar_perfil(request):

    user = request.user 
    if request.method =="POST":
        form = UserEditForm(request.POST) 

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            # user.password = info["password1"]
            user.save()
            return redirect("inicio")
        
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})
    return render(request, "editar_perfil.html", {"form":form})

# def crear_lector(request):
#     if request.method == "POST":
#         formulario = NuevoLector(request.POST)
#         if formulario.is_valid():
#             info_lector = formulario.cleaned_data
#             lector = Lector(nombre=info_lector["nombre"], apellido=info_lector["apellido"], email=info_lector["email"], edad=int(info_lector["edad"]), nacionalidad=info_lector["nacionalidad"])
#             lector.save()
#             return redirect("libros")
#         else:
#             redirect("crear_lector")

#     #GET Y OTROS METODOS
#     else:
#         formulariovacio = NuevoLector()
#         return render(request, "formulario_lector.html", {"form":formulariovacio})

