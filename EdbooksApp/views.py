import datetime
from tkinter.messagebox import NO
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, Template
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
            url = "/media/avatar/generica.png" 
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
            #image = form.cleaned_data.get('image')
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
            libros = Libro.objects.filter( Q(titulo__icontains=search) | Q(autor__icontains=search)).values()
            return render(request, "libros.html", {"libros":libros, "search":True, "busqueda":search})
        else:
            libros = Libro.objects.all()
            return render(request, "libros.html",{"libros":libros})

    elif request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url =  "/media/avatar/generica.png" 
    libros = Libro.objects.all()
    return render(request, "libros.html", {"url":url, "libros":libros})

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
        else:
            autores = Autores.objects.all()
            return render(request, "autores.html", {"autores":autores})

    elif request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url =  "/media/avatar/generica.png"
    autores = Autores.objects.all()
    return render(request, "autores.html", {"autores":autores, "url":url,})

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
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url =  "/media/avatar/generica.png"
        return render(request, "about.html", {"url":url})
    return render(request, "about.html", {"url":url})

def base(request):
    return render(request, "base.html", {})

def crear_libro(request):
    #POST
    if request.method == "POST":
        formulario = NuevoLibro(request.POST, request.FILES)
        if formulario.is_valid():
            info_libro = formulario.cleaned_data
            libro = Libro(titulo=info_libro["titulo"], autor=info_libro["autor"], año=int(info_libro["año"]), imagen=info_libro["imagen"], resumen=info_libro["resumen"])
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

@staff_member_required
def eliminar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    libro.delete()
    return redirect("libros")

def editar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    if request.method == "POST":
        formulario = NuevoLibro(request.POST, request.FILES)
        if formulario.is_valid():
            info_libro = formulario.cleaned_data
            libro.titulo = info_libro["titulo"]
            libro.autor = info_libro["autor"]
            libro.año = info_libro["año"]
            libro.resumen = info_libro["resumen"]
            libro.imagen = info_libro["imagen"]
            libro.save()
            return redirect("libros")


    #GET Y OTROS METODOS
    formulario = NuevoLibro(initial={"titulo":libro.titulo, "autor":libro.autor, "año":libro.año, "resumen":libro.resumen, "imagen":libro.imagen})
    return render(request,"formulario_libro.html",{"form":formulario})

@login_required
def editar_perfil(request):

    user = request.user 
    try:
        avatar = Avatar.objects.get(usuario=user)
    except:
        avatar = Avatar(usuario=user)
        avatar.save()
        #url = avatar.imagen.url

    if request.method =="POST":
        form = UserEditForm2(request.POST, request.FILES) 

        if form.is_valid():

            info = form.cleaned_data
            print(info["imagen"])
            print(request.FILES)
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            # user.password = info["password1"]
            user.save()
            if info['imagen'] != None:
                avatar.imagen = info['imagen']
                avatar.save()
            return redirect("inicio")
        else:
            print(form.errors)
            return render(request, "editar_perfil.html", {"form":form})

    else:
        form = UserEditForm2(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name, "imagen":avatar.imagen})
    return render(request, "editar_perfil.html", {"form":form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            #avatar.save()
            return redirect("inicio")
    else:
        form = AvatarForm()
    return render(request,"agregar_avatar.html",{"form":form})

class LibrosList(ListView):
    model = Libro
    template_name = "libros_list.html"

class LibroDetail(DetailView):
    model = Libro
    template_name = "libro_detail.html"

class LibroCreate(CreateView):
    model = Libro
    success_url = "/edbookapp/libro/list"
    fields = ["titulo", "autor", "año"]

class LibroUpdate(UpdateView):
    model = Libro
    success_url = "/edbookapp/libro/list"
    fields = ["titulo", "autor", "año"]

class LibroDelete(DeleteView):
    model = Libro
    success_url = "/edbookapp/libro/list"


