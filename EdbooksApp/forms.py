from tabnanny import verbose
from django import forms

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=50) #, verbose="Titulo:")
    autor = forms.CharField(max_length=70) #, verbose="Autor:")
    año = forms.IntegerField(min_value=0, label="Año de publicacion:") #, verbose="Año de publicacion:")
