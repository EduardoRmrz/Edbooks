from enum import auto
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    #URL de EdbooksApp
    path('libros/', libros, name="libros"),
    path('lectores/', lectores, name="lectores"),
    path('autores/', autor, name="autores"),
    path('about/', about, name="about"),
    path('base/', base),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    #path('crear_lector/', crear_lector, name="crear_lector"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),


    path('crear_libro/', crear_libro, name="crear_libro"),
    path('buscar_libro/', buscar_libro, name="buscar_libro"),
    path('crear_autor/', crear_autor, name="crear_autor"),
    path('buscar_autor/', buscar_autor, name="buscar_autor"),
    path('eliminar_autor/<autor_id>', eliminar_autor, name="eliminar_autor"),
    path('eliminar_libro/<libro_id>', eliminar_libro, name="eliminar_libro"),
    path('editar_libro/<libro_id>', editar_libro, name="editar_libro"),
    path('editar_autor/<autor_id>', editar_autor, name="editar_autor"),

    path('libro/list', LibrosList.as_view(), name="libro_list"),
    path(r'^(?P<pk>\d+)$', LibroDetail.as_view(), name="libro_detail"),
    path(r'^nuevo$', LibroCreate.as_view(), name="libro_create"),
    path(r'^editar/(?P<pk>\d+)$', LibroUpdate.as_view(), name="libro_update"),
    path(r'^eliminar/(?P<pk>\d+)$', LibroDelete.as_view(), name="libro_delete"),






]
