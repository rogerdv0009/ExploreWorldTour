from django.urls import path
from .views import *
urlpatterns = [
    path('listado/', VueloListView.as_view(), name="Vuelo_Listado"),
    path('crear/', VueloCreateView.as_view(), name="Vuelo_Crear"),
    path('editar/<int:pk>/', VueloUpdateView.as_view(), name="Vuelo_Editar"),
    path('eliminar/<int:pk>/', VueloDeleteView.as_view(), name="Vuelo_Eliminar"),
    path('detalle/<int:pk>/', VueloDetailView.as_view(), name="Vuelo_Detalle"),
    #////////////////////////////////////////////////////////////////////////////
    path('crear_reserva_vuelo/', Reserva_VueloCreateView.as_view(), name="Vuelo_Reserva"),
]