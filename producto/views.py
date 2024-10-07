from django.shortcuts import render
#Importamos HttpResponse
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación")

# Crear vista principal
def inicio(request):
    return render(request, 'base.html')