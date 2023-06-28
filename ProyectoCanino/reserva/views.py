
from django.views.generic import ListView, CreateView, UpdateView
from .models import Propietario, Mascota


class PropietarioListView(ListView):
    model = Propietario
    template_name = 'propietario_list.html'
    context_object_name = 'propietarios'


class PropietarioCreateView(CreateView):
    model = Propietario
    template_name = 'propietario_create.html'
    fields = ['nombre', 'direccion', 'telefono', 'correo']
    success_url = '/propietarios/'


class PropietarioUpdateView(UpdateView):
    model = Propietario
    template_name = 'propietario_update.html'
    fields = ['nombre', 'direccion', 'telefono', 'correo']
    success_url = '/propietarios/'


class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascota_list.html'
    context_object_name = 'mascotas'


class MascotaCreateView(CreateView):
    model = Mascota
    template_name = 'mascota_create.html'
    fields = ['nombre', 'raza', 'fecha_nacimiento', 'fecha_alojamiento', 'fecha_salida']
    success_url = '/mascotas/'


class MascotaUpdateView(UpdateView):
    model = Mascota
    template_name = 'mascota_update.html'
    fields = ['nombre', 'raza', 'fecha_nacimiento', 'fecha_alojamiento', 'fecha_salida']
    success_url = '/mascotas/'
