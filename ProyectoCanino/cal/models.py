# Modelo de evento: eventos del día, a qué hora comienza, finaliza y de qué se trata el evento.
from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# Definimos la propiedad get_html_url en el modelo Event que
# devuelve un enlace HTML para editar el evento
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,)) # El método reverse se utiliza para generar la URL de la vista de edición del evento (cal:event_edit) y se pasa el argumento self.id para especificar el ID del evento en la URL
        return f'<a href="{url}"> {self.title} </a>'
