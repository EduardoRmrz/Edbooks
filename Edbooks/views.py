from django.http import HttpResponse
from django.template import Template, Context

def primera_view(request):
    return HttpResponse("saludos")

def segunda_vista(request):
    with open("index.html") as file:
        plantilla = Template(file.read())
        contexto = Context()
        documento = plantilla.render(contexto)
        return HttpResponse(documento)