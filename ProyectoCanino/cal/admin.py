# Registramos el modelo eventos para agregar eventos a través de la interfaz de administración
from django.contrib import admin
from cal.models import Event

admin.site.register(Event)