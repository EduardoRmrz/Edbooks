import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
def inicio(request):
    hoy = datetime.datetime.now()
    return render(request, "index.html", {"dia_hora":hoy})

