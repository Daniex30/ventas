from django.urls import path
from .  import views

app_name = "producto_app"

urlpatterns = [
    # categoria
    path('crear_categoria/', views.CategoriaCreateView.as_view(), name="crear_categoria"),
    path('listar_categoria/', views.CategoriaListView.as_view(), name="listar_categorias"),
    path('actualizar_categoria/<pk>', views.CategoriaUpdateView.as_view(), name="actualizar_categoria"),
    
    # marca
    path('crear_marca/', views.MarcaCreateView.as_view(), name="crear_marca"),
    path('listar_marca/', views.MarcaListView.as_view(), name="listar_marcas"),
    path('actualizar_marca/<pk>', views.MarcaUpdateView.as_view(), name="actualizar_marca"),

    # estado
    path('crear_estado/', views.EstadoCreateView.as_view(), name="crear_estado"),

    # producto
    path('listar_producto/', views.ProductoListView.as_view(), name="listar_productos"),
    path('crear_producto/', views.ProductoCreateView.as_view(), name="crear_producto"),
    path('actualizar_producto/<pk>', views.ProductoUpdateView.as_view(), name="actualizar_producto"),
    path('bloquear_producto/<pk>', views.ProductoBlockView.as_view(), name="bloquear_producto"),
]