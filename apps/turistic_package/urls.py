from django.urls import path
from .views import (PaqueteTuristicoListView,PaqueteTuristicoCreateView, 
                    PaqueteTuristicoDetailView, PaqueteTuristicoUpdateView,
                    PaqueteTuristicoDeleteView, LocacionTuristicaCreateView, 
                    PaisCreateView, Reserva_PaqueteCreateView)
urlpatterns = [
    #Urls Para Los Paquetes Turisticos
    path('listado/', PaqueteTuristicoListView.as_view(), name="Paquete_Listado"),
    path('crear/', PaqueteTuristicoCreateView.as_view(), name="Paquete_Crear"),
    path('detalle/<int:pk>/', PaqueteTuristicoDetailView.as_view(), name="Paquete_Detalle"),
    path('editar/<int:pk>/', PaqueteTuristicoUpdateView.as_view(), name="Paquete_Editar"),
    path('eliminar/<int:pk>/', PaqueteTuristicoDeleteView.as_view(), name="Paquete_Eliminar"),
    #///////////////////////////////////////////////////////////////////////////////////
    path('crear_locacion/', LocacionTuristicaCreateView.as_view(), name="Locacion_Crear"),
    #//////////////////////////////////////////////////////////////////////////////////'
    path('crear_pais/', PaisCreateView.as_view(), name="Pais_Crear"),
    #//////////////////////////////////////////////////////////////////////////////////
    path('crear_reserva/', Reserva_PaqueteCreateView.as_view(), name="Paquete_Reserva"),
]