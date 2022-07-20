from enum import auto
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    #URL de EdbooksApp
    path('libros/', libros, name="libros"),
    path('usuarios/', usuarios, name="usuarios"),
    path('autores/', autor, name="autores"),
    path('about/', about, name="about"),
    path('base/', base),
    path('crear_libro/', crear_libro, name="crear_libro"),
    path('buscar_libro/', buscar_libro, name="buscar_libro"),
]
