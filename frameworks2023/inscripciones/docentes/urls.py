from django.urls import path, include
from docentes import views

#app_name = 'docentes'

urlpatterns = [
    path('', views.ListaDocente.as_view(), name='lista_docentes'),
    path('nuevo/', views.NuevoDocente.as_view(), name='nuevo_docente'),
    path('municipios', views.busca_municipios, name='busca_municipios'),
]