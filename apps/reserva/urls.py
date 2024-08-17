from django.urls import path
from .views import *
urlpatterns = [
    path('listar_reserva/', ReservasView.as_view(), name="Reserva_Listado"),
    #Urls Para Las Reservas de Paquetes
    path('eliminar_reserva_paquete/<int:pk>/', Reserva_PaqueteDeleteView.as_view(), name="Reserva_Paquete_Eliminar"),
    path('editar_reserva_paquete/<int:pk>/', Reserva_PaqueteUpdateView.as_view(), name="Reserva_Paquete_Editar"),
    path('crear_reserva_paquete/', Reserva_PaqueteCreateView.as_view(), name="Reserva_Paquete_Crear"),
    path('listar_reserva_paquete/', Reserva_PaqueteListView.as_view(), name="Reserva_Paquete_Listado"),
    #/////////////////////////////////////////////////////////////////////////////////////////////
    #Urls Para Los Vuelos
    path('eliminar_reserva_vuelo/<int:pk>/', Reserva_VueloDeleteView.as_view(), name="Reserva_Vuelo_Eliminar"),
    path('editar_reserva_vuelo/<int:pk>/', Reserva_VueloUpdateView.as_view(), name="Reserva_Vuelo_Editar"),
    path('crear_reserva_vuelo/', Reserva_VueloCreateView.as_view(), name="Reserva_Vuelo_Crear"),
    path('listar_reserva_vuelo/', Reserva_VueloListView.as_view(), name="Reserva_Vuelo_Listado"),
    #/////////////////////////////////////////////////////////////////////////////////////////////
]