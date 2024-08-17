from django.db import models
from apps.main.models import Modelo_Base
from apps.turistic_package.models import Paquete_Turistico
from apps.vuelo.models import Vuelo
from apps.users.models import Usuario
# Create your models here.

class Reserva_Vuelo(Modelo_Base):

    vuelo = models.ForeignKey(Vuelo, verbose_name="Vuelo", on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.CASCADE)
    cancelada = models.BooleanField("Cancelar Reserva",default = False, null=False,blank=False)
    aceptada = models.BooleanField("Aceptar Reserva",default = False, null=False,blank=False)
    
    class Meta:
        verbose_name = "Reserva_Vuelo"
        verbose_name_plural = "Reservas_Vuelos"
    
    def __str__(self):
        return f'Reserva del vuelo: {self.vuelo}'

class Reserva_Paquete(Modelo_Base):

    nombre_paquete = models.ForeignKey(Paquete_Turistico, verbose_name="Paquete Turístico", on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, verbose_name='Usuario', on_delete=models.CASCADE)
    cancelada = models.BooleanField("Cancelar Reserva", default = False, null=False, blank=False)
    aceptada = models.BooleanField("Aceptar Reserva", default = False, null=False, blank=False)
    
    class Meta:
        verbose_name = "Reserva_Paquete"
        verbose_name_plural = "Reservas_Paquetes"

    def __str__(self):
        return f'Reserva del paquete turístico: {self.nombre_paquete}'



