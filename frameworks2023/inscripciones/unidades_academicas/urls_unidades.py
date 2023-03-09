from django.urls import path
from unidades_academicas import views

urlpatterns = [
    path('', views.lista_unidades, name='lista_unidades'),
    path('nueva', views.nueva_unidad, name='nueva_unidad'),
    path('eliminar/<int:id>', views.eliminar_unidad, name='eliminar_unidad'),
    path('editar/<int:id>', views.editar_unidad, name='editar_unidad'),
]