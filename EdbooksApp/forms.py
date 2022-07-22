from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=50) #, verbose="Titulo:")
    autor = forms.CharField(max_length=70) #, verbose="Autor:")
    año = forms.IntegerField(min_value=0, label="Año de publicacion:") #, verbose="Año de publicacion:")

class NuevoAutor(forms.Form):
    nombre = forms.CharField(max_length=50) #, verbose="Titulo:")
    apellido = forms.CharField(max_length=70) #, verbose="Autor:")
    nacionalidad = forms.CharField(max_length=50, label="Pais de residencia:")

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellidos", required=False)

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}