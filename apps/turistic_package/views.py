from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from apps.reserva.forms import Reserva_Paquete_Form
from apps.reserva.models import Reserva_Paquete
from apps.users.models import Usuario
from .models import Paquete_Turistico, Locacion_Turistica, Pais
from .forms import Paquete_TuristicoForm, Locacion_TuristicaForm, PaisForm

# Create your views here.

# Vistas de los paquetes Turisticos

class PaqueteTuristicoListView(ListView):
    model = Paquete_Turistico
    template_name = "turistic_package/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
  
class PaqueteTuristicoCreateView(CreateView):
    model = Paquete_Turistico
    template_name = "turistic_package/crear_paquete.html"
    form_class = Paquete_TuristicoForm
    success_url = reverse_lazy("Paquete_Listado")  
    
class PaqueteTuristicoDetailView(DetailView):
    model = Paquete_Turistico
    template_name = "turistic_package/detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservas"] = Reserva_Paquete.objects.all()
        return context
    
    
class PaqueteTuristicoUpdateView(UpdateView):
    model = Paquete_Turistico
    template_name = "turistic_package/editar_paquete.html"
    form_class = Paquete_TuristicoForm
    success_url = reverse_lazy("Paquete_Listado")

class PaqueteTuristicoDeleteView(DeleteView):
    model = Paquete_Turistico
    template_name = "turistic_package/eliminar_paquete.html"
    
    def post(self, request, pk, *args, **kwargs):
        object = Paquete_Turistico.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Paquete_Listado')


# Vistas de las Locaciones Turisticas

class LocacionTuristicaCreateView(CreateView):
    model = Locacion_Turistica
    template_name = "turistic_package/locacion_turistica/crear_locacion.html"
    form_class = Locacion_TuristicaForm
    success_url = reverse_lazy("Paquete_Listado")
    


# Vistas de los Paises

class PaisCreateView(CreateView):
    model = Pais
    template_name = "turistic_package/pais/crear_pais.html"
    form_class = PaisForm
    success_url = reverse_lazy("Paquete_Listado")
    
    
#Vista para crear reserva de paquetes

class Reserva_PaqueteCreateView(View):
    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario POST
        user = request.POST.get('input_user')
        nombre_paquete = request.POST.get('input_paquete')
        reservas_hechas = Reserva_Paquete.objects.filter(user = user, nombre_paquete = nombre_paquete)
        if reservas_hechas:
            return HttpResponse('Ya el usuario realizo una reserva de este paquete con anterioridad')
        # Crear una nueva instancia de TuModelo con los datos recibidos
        usuario = Usuario.objects.get(pk = user)
        paquete_t = Paquete_Turistico.objects.get(id = nombre_paquete)
        nueva_instancia = Reserva_Paquete(user=usuario, nombre_paquete=paquete_t)
        nueva_instancia.save()

        return redirect('Paquete_Listado')