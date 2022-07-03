from django.shortcuts import render, HttpResponse
from servicios.models import Servicio 

# Create your views here.
def home(request):
    
    return render(request, "appweb/home.html")

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "appweb/servicios.html", {"servicios": servicios})

def tienda(request):
    
    return render(request, "appweb/tienda.html")

def blog(request):
    
    return render(request, "appweb/blog.html")

def contacto(request):
    
    return render(request, "appweb/contacto.html")
