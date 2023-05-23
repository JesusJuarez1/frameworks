from rest_framework import serializers
from materias.models import Materia


class SerializerMateria(serializers.ModelSerializer):
    
    class Meta:
        model = Materia
        fields = '__all__'
        # fields = ['clave','nombre', 'creditos', 'semestre']

