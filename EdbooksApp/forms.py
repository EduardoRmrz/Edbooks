from tabnanny import verbose
from django import forms

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=50) #, verbose="Titulo:")
    autor = forms.CharField(max_length=70) #, verbose="Autor:")
    año = forms.IntegerField(min_value=0, label="Año de publicacion:") #, verbose="Año de publicacion:")

class NuevoAutor(forms.Form):
    nombre = forms.CharField(max_length=50) #, verbose="Titulo:")
    apellido = forms.CharField(max_length=70) #, verbose="Autor:")
    nacionalidad = forms.CharField(max_length=50, label="Pais de residencia:")