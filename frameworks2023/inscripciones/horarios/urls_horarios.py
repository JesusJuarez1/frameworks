from django.urls import path, include
from horarios import views

urlpatterns = [
    path('', views.ListaHorarios.as_view(), name='lista_horarios'),
    path('nuevo/', views.NuevoHorario.as_view(), name='nuevo_horario'),
    path('editar/<str:pk>', views.EditarHorario.as_view(), name='editar_horario'),
    path('eliminar/<str:pk>', views.EliminarHorario.as_view(), name='eliminar_horario')
]
