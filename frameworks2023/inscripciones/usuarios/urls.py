from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('nuevo_docente/', views.RegistrarDocente.as_view(), name='nuevo_docente'),
    path('perfil', views.perfil, name='perfil_docente'),
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuenta.as_view(), name='activar'),
    path('lista', views.lista_usuarios, name='lista_usuarios'),
    path('grupo_usuarios', views.asignar_grupo_usuarios, name='grupo_usuarios'),
    
    # path('nuevo-alumno/', views.RegistrarAlumno.as_view(), name='nuevo_alumno'),
]
