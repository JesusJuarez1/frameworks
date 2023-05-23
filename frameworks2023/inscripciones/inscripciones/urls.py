from django.contrib import admin
from django.urls import path, include
from materias.views import Bienvenida
from rest_framework import routers
from api import views

# METHODS
# GET POST PUT PATCH DELETE
router = routers.DefaultRouter()
router.register(r'', views.MateriaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('programas/', include('programas.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls')),
    path('', Bienvenida.as_view(), name='bienvenida'),
    path('horarios/', include('horarios.urls_horarios')),
    path('usuarios/', include('usuarios.urls')),
    path('materias-api/', include(router.urls)),
]
