from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Reserva_Paquete, Reserva_Vuelo
from .forms import Reserva_Paquete_Form, Reserva_Vuelo_Form, SelectForm
 # Create your views here.
#View para renderizar las reservas de vuelos y paquetes turisticos
class ReservasView(TemplateView):
    template_name = "reserva/listar_reserva.html"

 #Reservas de Paquetes Turisticos
class Reserva_PaqueteListView(ListView):
    model = Reserva_Paquete
    template_name = "reserva/paquete/reserva_listado_paquete.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('Filtrado_Reserva')
        if valor_select == 'Reservas en espera':
            queryset = queryset.filter(cancelada = False, aceptada = False)
        elif valor_select == 'Reservas canceladas':
            queryset = queryset.filter(cancelada = True, aceptada = False)
        elif valor_select == 'Reservas aceptadas':
            queryset = queryset.filter(cancelada = False, aceptada = True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_reserva"] = SelectForm
        return context

class Reserva_PaqueteUpdateView(UpdateView):
    model = Reserva_Paquete
    template_name = "reserva/paquete/editar_reserva_paquete.html"
    form_class = Reserva_Paquete_Form
    success_url = reverse_lazy("Reserva_Paquete_Listado")

class Reserva_PaqueteCreateView(CreateView):
    model = Reserva_Paquete
    template_name = "reserva/paquete/crear_reserva_paquete.html"
    form_class = Reserva_Paquete_Form
    success_url = reverse_lazy("Reserva_Paquete_Listado")

class Reserva_PaqueteDeleteView(DeleteView):
    model = Reserva_Paquete
    template_name = "reserva/paquete/eliminar_reserva_paquete.html"
    success_url = reverse_lazy("Reserva_Paquete_Listado")


#/////////////////////////////////////////////////////////////////////////////////////////////

#Reservas de Vuelos
class Reserva_VueloListView(ListView):
    model = Reserva_Vuelo
    template_name = "reserva/vuelo/reserva_listado_vuelo.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('Filtrado_Reserva')
        if valor_select == 'Reservas en espera':
            queryset = queryset.filter(cancelada = False, aceptada = False)
        elif valor_select == 'Reservas canceladas':
            queryset = queryset.filter(cancelada = True, aceptada = False)
        elif valor_select == 'Reservas aceptadas':
            queryset = queryset.filter(cancelada = False, aceptada = True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_reserva"] = SelectForm
        return context
    
class Reserva_VueloCreateView(CreateView):
    model = Reserva_Vuelo
    template_name = "reserva/vuelo/crear_reserva_vuelo.html"
    form_class = Reserva_Vuelo_Form
    success_url = reverse_lazy("Reserva_Vuelo_Listado")

class Reserva_VueloUpdateView(UpdateView):
    model = Reserva_Vuelo
    template_name = "reserva/vuelo/editar_reserva_vuelo.html"
    form_class = Reserva_Vuelo_Form
    success_url = reverse_lazy("Reserva_Vuelo_Listado")
    
class Reserva_VueloDeleteView(DeleteView):
    model = Reserva_Vuelo
    template_name = "reserva/vuelo/eliminar_reserva_vuelo.html"
    success_url = reverse_lazy("Reserva_Vuelo_Listado")
