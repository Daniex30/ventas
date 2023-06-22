from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import(
    TemplateView
)
# Create your views here.
class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('user_app:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nombre = self.request.session.get('nombre')
        apellido = self.request.session.get('apellido')
        exito = self.request.session.get('exito')
        if nombre:
            context['nombre'] = nombre
            del self.request.session['nombre']
            context['apellido'] = apellido
            del self.request.session['apellido'] 
        elif exito:
            context['exito'] = exito
            del self.request.session['exito']
        return context
