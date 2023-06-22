from django.urls import path
from .  import views

app_name = "user_app"

urlpatterns = [
    path('registro/', views.UserRegisterView.as_view(), name="registro"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name= "logout"),
    path('actualizar_contraseña/', views.UpdatePasswordView.as_view(), name= "update_pass"),
    path('actualizar_datos/<pk>', views.UpdateUserView.as_view(), name= "update_user"),
    path('lista_usuarios/', views.ListUserView.as_view(), name= "panel"),
    path('bloquear_usuario/<pk>', views.BlockUserView.as_view(), name= "block_user"),
    path('actualizar_rol/<pk>', views.UpdateRolUserView.as_view(), name= "update_rol"),
]