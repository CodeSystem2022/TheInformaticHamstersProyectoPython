from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})
                                                                        #con esto cargamos la variable servicios que es

                                                                #la que importa todos los servicios de la clase Servicios