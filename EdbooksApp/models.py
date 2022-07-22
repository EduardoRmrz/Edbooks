from django.db import models
from django.forms import IntegerField

#modelo de avtar


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
