from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView

from apps.turistic_package.models import Paquete_Turistico
from apps.vuelo.models import Vuelo
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('Paquete_Listado')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
class CerrarSesion(RedirectView):
    pattern_name = 'Login'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ultimo_paquete"] = Paquete_Turistico.objects.filter(estado = True).first()
        context["cant_paquete"] = Paquete_Turistico.objects.filter(estado = True).count()
        context["calificacion_paquete"] = Paquete_Turistico.objects.filter(calificacion__gt = 3).count()
        context["ultimo_vuelo"] = Vuelo.objects.filter(estado = True).first()
        context["cant_vuelo"] = Vuelo.objects.filter(estado = True).count()
        return context
    