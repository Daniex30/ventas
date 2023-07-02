from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View, UpdateView, ListView
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, UpdateUserForm
from .models import User
from .mixins import AdministradorPermisoMixin

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'users/registro.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_app:panel')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        User.object.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            # se asigna el contnido de rol a una variable devido a que es un extra_fields
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            rol=form.cleaned_data['rol'],
        )
        self.request.session['nombre'] = nombre
        self.request.session['apellido'] = apellido
        return super(UserRegisterView, self).form_valid(form)
    
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user_app:panel')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutView(View):

    def get(self, request, *args, **kwords):
        logout(request)
        return HttpResponseRedirect(
            reverse('user_app:login')
        )
    

class UpdatePasswordView(LoginRequiredMixin,FormView):
    template_name = 'users/actualizar_contrasena.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('user_app:panel')
    login_url = reverse_lazy('user_app:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email= usuario.email,
            password=form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
    
class UpdateUserView(UpdateView):
    template_name = "users/actualizar_datos.html"
    model = User
    form_class= UpdateUserForm
    
    success_url = reverse_lazy('user_app:panel')

    # usamos form valid para crear una variable de session
    def form_valid(self, form):
        self.request.session['exito'] = True
        return super().form_valid(form)
    

class ListUserView(ListView):
    template_name = 'users/lista_usuarios.html'
    content_object_name = "users"
    model = User
    paginate_by = 12

    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return User.object.buscar_nombre_apellido(palabra_clave)
    
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
    
        
class BlockUserView(AdministradorPermisoMixin, UpdateView):
    template_name = 'users/bloquear_usuario.html'
    model = User
    fields = ["is_active"]
    success_url = reverse_lazy('user_app:panel')

class UpdateRolUserView(UpdateView):
    template_name = 'users/actualizar_rol.html'
    model = User
    fields = ["rol"]
    success_url = reverse_lazy('user_app:panel')