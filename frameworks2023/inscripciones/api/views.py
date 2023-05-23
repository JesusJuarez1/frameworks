from django.shortcuts import render
from . serializers import SerializerMateria
from rest_framework import permissions, viewsets
from materias.models import Materia


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all().order_by('nombre')
    serializer_class = SerializerMateria
    permission_classes = [permissions.IsAuthenticated]





