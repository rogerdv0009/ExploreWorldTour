from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.main.models import Modelo_Base
# Create your models here.

class Pais(Modelo_Base):

    nombre = models.CharField("Nombre del País", max_length=50, null = False, blank = False)
    estado_pais = models.CharField("Estado del País", max_length=150, null = False, blank = False)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Paises"

    def __str__(self):
        return f'{self.nombre} / {self.estado_pais}'




class Locacion_Turistica(Modelo_Base):

    nombre_locacion = models.CharField("Locación Turística", max_length=150, null = False, blank = False)
    pais = models.ForeignKey(Pais, verbose_name="País", on_delete=models.CASCADE, null = False, blank = False)

    class Meta:
        verbose_name = "Locacion_Turistica"
        verbose_name_plural = "Locaciones_Turisticas"

    def __str__(self):
        return self.nombre_locacion



class Paquete_Turistico(Modelo_Base):
    
    locacion_turistica = models.ForeignKey(Locacion_Turistica, verbose_name="Locación Turística", on_delete=models.CASCADE)
    actividades = models.CharField("Actividades", max_length=250)
    estancia = models.CharField("Estancia", max_length=150, blank = False, null = False)
    precio = models.PositiveIntegerField("Precio", blank = False, null = False)
    tiempo_estancia = models.PositiveIntegerField("Tiempo de Estancia", blank = False, null = False)
    calificacion = models.PositiveIntegerField("Calificación", blank = False, null = False, default=4, validators=[MinValueValidator(0),MaxValueValidator(5)])
    imagen_paquete = models.ImageField("Imagen", upload_to='paquetes_turisticos/', null=True, blank=True)
    fecha_entrada = models.DateField("Fecha de Entrada", auto_now=False, auto_now_add=False)
    fecha_salida = models.DateField("Fecha de Salida", auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = "Paquete_Turístico"
        verbose_name_plural = "Paquetes_Turísticos"
        ordering= ['-id']
        
    def NochesEstancias(self):
        noches = self.tiempo_estancia - 1
        return noches
    
    def __str__(self):
        return f'Paquete Turístico: {self.locacion_turistica}'

