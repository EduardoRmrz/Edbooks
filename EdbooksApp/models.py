from distutils.command.upload import upload
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

#modelo de avtar
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"
    class Meta:
        verbose_name_plural = "Avatares"

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=70)
    año = models.IntegerField()
    resumen = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to="portadas", null=True, blank=True)

class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    edad = models.IntegerField(null=True)
    #nacionalidad = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Lectores"

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    #libros_escritos = IntegerField(min_value=0)

    class Meta:
        verbose_name_plural = "Autores"
