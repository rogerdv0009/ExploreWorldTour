from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from apps.reserva.forms import Reserva_Vuelo_Form
from apps.reserva.models import Reserva_Vuelo
from apps.users.models import Usuario
from .models import Vuelo
from .forms import VueloForm

# Create your views here.

class VueloListView(ListView):
    model = Vuelo
    template_name = "vuelo/listado_vuelo.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
  
class VueloCreateView(CreateView):
    model = Vuelo
    template_name = "vuelo/crear_vuelo.html"
    form_class = VueloForm
    success_url = reverse_lazy("Vuelo_Listado")
    
class VueloDetailView(DetailView):
    model = Vuelo
    template_name = "vuelo/detalle_vuelo.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservas"] = Reserva_Vuelo.objects.all()
        return context
    
class VueloUpdateView(UpdateView):
    model = Vuelo
    template_name = "vuelo/editar_vuelo.html"
    form_class = VueloForm
    success_url = reverse_lazy("Vuelo_Listado")

class VueloDeleteView(DeleteView):
    model = Vuelo
    template_name = "vuelo/eliminar_vuelo.html"
    
    def post(self, request, pk, *args, **kwargs):
        object = Vuelo.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Vuelo_Listado')


# Vista para crear reserva de vuelo

class Reserva_VueloCreateView(View):
    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario POST
        user = request.POST.get('input_user_vuelo')
        nombre_paquete = request.POST.get('input_vuelo')
        reservas_hechas = Reserva_Vuelo.objects.filter(user = user, vuelo = nombre_paquete)
        if reservas_hechas:
            return HttpResponse('Ya el usuario realizó una reserva de este paquete con anterioridad')
        # Crear una nueva instancia de Reserva con los datos recibidos
        usuario = Usuario.objects.get(pk = user)
        paquete_t = Vuelo.objects.get(id = nombre_paquete)
        nueva_instancia = Reserva_Vuelo(user=usuario, vuelo=paquete_t)
        nueva_instancia.save()

        return redirect('Vuelo_Listado')