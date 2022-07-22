from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

#modelo de avtar
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=70)
    año = models.IntegerField()

class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    edad = models.IntegerField(null=True)
    #nacionalidad = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "LEctores"

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Autores"
