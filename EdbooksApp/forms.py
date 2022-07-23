from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from EdbooksApp.models import Avatar

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=50) #, verbose="Titulo:")
    autor = forms.CharField(max_length=70) #, verbose="Autor:")
    año = forms.IntegerField(min_value=0, label="Año de publicacion:") #, verbose="Año de publicacion:")

class NuevoAutor(forms.Form):
    nombre = forms.CharField(max_length=50) #, verbose="Titulo:")
    apellido = forms.CharField(max_length=70) #, verbose="Autor:")
    nacionalidad = forms.CharField(max_length=50, label="Pais de residencia:")

class UserRegisterForm(UserCreationForm):
    
    foto = forms.ImageField(required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellidos", required=False)

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
        email = forms.EmailField(label="Email")
        password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
        password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

        first_name = forms.CharField(label="Nombre")
        last_name = forms.CharField(label="Apellido")

        class Meta:
            model = User
            fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

            help_texts = {k:"" for k in fields}

# class NuevoLector(forms.Form):
#     nombre = forms.CharField(max_length=50) #, verbose="Titulo:")
#     apellido = forms.CharField(max_length=70) #, verbose="Autor:")
#     edad = forms.IntegerField(min_value=0, label="Edad: ")
#     email = forms.EmailField(label="Email: ")
#     nacionalidad = forms.CharField(max_length=50, label="Pais de residencia:")

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="imagen")
    class Meta:
        model = Avatar
        fields = ['imagen']