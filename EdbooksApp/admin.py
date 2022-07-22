from django.contrib import admin
from EdbooksApp.models import *

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'año')
    search_fields = ('titulo', 'autor')
admin.site.register(Libro, LibroAdmin)

class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'edad')
admin.site.register(Lector,LectorAdmin)

class AutoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
admin.site.register(Autores, AutoresAdmin)