from django.db import models
from apps.main.models import Modelo_Base
from apps.turistic_package.models import Pais
# Create your models here.

aerolineas_vuelo = {
    ('Air Europa', 'Air Europa'),
    ('Interjet', 'Interjet'),
    ('Delta Airlines', 'Delta Airlines'),
}
    
class Vuelo(Modelo_Base):

    destino = models.ForeignKey(Pais, verbose_name="Destino", on_delete=models.CASCADE, null = False, blank = False)
    fecha_salida = models.DateTimeField("Fecha de Salida", auto_now=False, auto_now_add=False, null = False, blank = False)
    precio = models.PositiveIntegerField("Precio del Vuelo", null = False, blank = False)
    aerolinea = models.CharField("Aerolínea", max_length=50, choices = aerolineas_vuelo)
    imagen_vuelo = models.ImageField("Imagen", upload_to="vuelos/", null=True,blank=True)

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"
        ordering= ['-id']

    def __str__(self):
        return f'Vuelo con Destino a: {self.destino} por la aerolinea: {self.aerolinea}'

