from typing import Any
from django import http
from django.http.response import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import User

def verificar_rol(rol, usuario_rol):
    # 
    if(rol == 'Administrador' or rol == usuario_rol):
        return True
    else:
        return False
    
class AdministradorPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not verificar_rol(request.user.rol.nombre, 'Administrador'):
            return HttpResponseRedirect(
                reverse(
                    'user_app:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)
    
class VentaPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not verificar_rol(request.user.rol.nombre, 'Venta'):
            return HttpResponseRedirect(
                reverse(
                    'user_app:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)
    
class SacPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not verificar_rol(request.user.rol.nombre, 'SAC'):
            return HttpResponseRedirect(
                reverse(
                    'user_app:login'
                )
            )
        return super().dispatch(request, *args, **kwargs)