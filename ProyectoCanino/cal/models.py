# Modelo de evento: eventos del día, a qué hora comienza, finaliza y de qué se trata el evento.
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
