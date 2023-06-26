from django.urls import path
from .views import Registro, cerrar_sesion, loguear

urlpatterns = [
   path('', Registro.as_view(), name="Usuario"),
   path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
   path('loguear', loguear, name="loguear"),
]

