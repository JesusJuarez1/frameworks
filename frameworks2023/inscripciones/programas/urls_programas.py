from django.urls import path
from programas import views

urlpatterns = [
    path('', views.lista_programas, name='lista_programas'),
    path('nuevo', views.nuevo_programa, name='nuevo_programa'),
    path('eliminar/<int:clave>', views.eliminar_programa, name='eliminar_programa'),
    path('editar/<int:clave>', views.editar_programa, name='editar_programa'),
]