"""
URL configuration for agencia_viaje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.views.static import serve
from django.contrib.auth.views import logout_then_login
from agencia_viaje.settings import base 
from apps.main.views import LoginFormView, CerrarSesion, HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name="Home"),
    path('login/', LoginFormView.as_view(), name="Login"),
    path('logout/', CerrarSesion.as_view(), name='Logout'),
    path('paquetes_turisticos/', include('apps.turistic_package.urls')),
    path('vuelos/', include('apps.vuelo.urls')),
    path('reservas/', include('apps.reserva.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': base.MEDIA_ROOT,
    })
]