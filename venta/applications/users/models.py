from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.


class Rol(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    object = UserManager()

    def __str__(self):
        return self.username + ' ' + self.email + ' ' +  self.nombre + ' ' + self.apellido

    def get_fullname(self):
        return self.nombre + ' ' + self.apellido
    
    def get_rol(self):
        return self.rol