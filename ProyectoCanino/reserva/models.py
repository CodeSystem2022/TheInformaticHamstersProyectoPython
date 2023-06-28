

# Modelo propietario
from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo Mascota
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    fecha_alojamiento = models.DateField()
    fecha_salida = models.DateField()

    # Campos adicionales
    alergias = models.TextField(blank=True)
    medicamentos = models.TextField(blank=True)
    condiciones_medicas = models.TextField(blank=True)
    tipo_comida = models.CharField(max_length=100, blank=True)
    horarios_alimentacion = models.CharField(max_length=100, blank=True)
    servicios_adicionales = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

