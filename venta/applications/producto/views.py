from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Marca, Estado, Producto
from .forms import CategoriaForm, MarcaForm, EstadoForm, ProductoForm, UpdateProductForm, BlockProductForm
from applications.users.mixins import AdministradorPermisoMixin
from django.views.generic import (
    CreateView, ListView, UpdateView
    )

# Create your views here.

# categoria
class CategoriaCreateView(AdministradorPermisoMixin, CreateView):
    template_name = 'producto/crear_categoria.html'
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('producto_app:listar_categorias')

class CategoriaListView(AdministradorPermisoMixin, ListView):
    template_name = 'producto/listar_categorias.html'
    model = Categoria
    context_object_name = 'categorias'
    ordering = 'id'

class CategoriaUpdateView(AdministradorPermisoMixin, UpdateView):
    template_name = 'producto/actualizar_categoria.html'
    model = Categoria
    fields = ['nombre']
    success_url = reverse_lazy('producto_app:listar_categorias')

# marca

class MarcaCreateView(AdministradorPermisoMixin,CreateView):
    template_name = 'producto/crear_marca.html'
    model = Marca
    form_class = MarcaForm
    success_url = reverse_lazy('producto_app:listar_marcas')

class MarcaListView(AdministradorPermisoMixin,ListView):
    template_name = 'producto/listar_marcas.html'
    model = Marca
    context_object_name = 'marcas'
    ordering = 'id'


class MarcaUpdateView(AdministradorPermisoMixin,UpdateView):
    template_name = 'producto/actualizar_marca.html'
    model = Marca
    fields = ['nombre']
    success_url = reverse_lazy('producto_app:listar_marcas')

# estado 

class EstadoCreateView(AdministradorPermisoMixin,CreateView):
    template_name = 'producto/crear_estado.html'
    model = Estado
    form_class = EstadoForm
    success_url = reverse_lazy('producto_app:listar_marcas')

# producto

class ProductoListView(AdministradorPermisoMixin,ListView):
    template_name = 'producto/listar_productos.html'
    model = Producto
    context_object_name = 'productos'
    ordering = 'nombre'
    paginate_by = 10

class ProductoCreateView(AdministradorPermisoMixin, CreateView):
    template_name = 'producto/crear_producto.html'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:listar_productos')

class ProductoUpdateView(AdministradorPermisoMixin,UpdateView):
    template_name = 'producto/actualizar_producto.html'
    model = Producto
    form_class = UpdateProductForm
    success_url = reverse_lazy('producto_app:listar_productos')

class ProductoBlockView(AdministradorPermisoMixin,UpdateView):
    template_name = 'producto/block_producto.html'
    model = Producto
    form_class = BlockProductForm
    success_url = reverse_lazy('producto_app:listar_productos')
