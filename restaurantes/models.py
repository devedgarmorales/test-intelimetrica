from django.db import models
import uuid
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.
class Restaurante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clasificacion = models.IntegerField()
    nombre = models.CharField(max_length=255)
    sitio = models.URLField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    ubicacion = models.PointField(geography=True, default=Point(0, 0))

    def __str__(self):
        return self.nombre