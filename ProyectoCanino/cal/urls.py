# agregamos la vista index

from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # se define dos URL: una para crear un evento nuevo y otra para editar un evento existente.
    # Los patrones de URL capturan el ID del evento como parte de la URL y lo pasan como argumento a la vista event
    # para determinar si se está creando un evento nuevo o editando uno existente.
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
]
