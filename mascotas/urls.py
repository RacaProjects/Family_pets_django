from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'mascotas'
urlpatterns = [
    path('', views.index, name='index'),
    path('ver-mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/', views.lista_mascotas, name='lista'),
    path('nuevo/', views.crear_mascota, name='nuevo'),
    path('editar/<int:pk>/', views.editar_mascota, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar'),
    path('detalle/<int:pk>/', views.detalle_mascota, name='detalle'),
    path('login/', auth_views.LoginView.as_view(template_name='mascotas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mascotas:index'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('detalle/<int:pk>/', views.detalle_mascota, name='detalle'),
]


