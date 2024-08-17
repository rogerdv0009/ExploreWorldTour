from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

rol_usuario={
    ('Gestor de Venta','Gestor de Venta'),
    ('Administrador','Administrador'),
    ('Usuario del sistema','Usuario del sistema')
}

class Usuario(AbstractUser):

    rol = models.CharField("Rol de Usuario", max_length=50, choices=rol_usuario, null = False, blank = False)
    imagen_usuario = models.ImageField("Imagen", upload_to='usuarios/', null=True,blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return self.username

